from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from profiles.models import Profile

from .models import Rating

User = get_user_model()

# create agent review
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, profile_id):
    service_provider_profile = Profile.objects.get(id=profile_id, is_service_provider=True)
    data = request.data

    profile_user = User.objects.get(pkid=service_provider_profile.user.pkid)
    if profile_user.email == request.user.email:
        formatted_response = {"message": "You can't rate yourself"}
        return Response(formatted_response, status=status.HTTP_403_FORBIDDEN)

    alreadyExists = service_provider_profile.agent_review.filter(
        agent__pkid=profile_user.pkid
    ).exists()

    if alreadyExists:
        formatted_response = {"detail": "Profile already reviewed"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    elif data["rating"] == 0:
        formatted_response = {"detail": "Please select a rating"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    else:
        review = Rating.objects.create(
            rater=request.user,
            agent=service_provider_profile,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = service_provider_profile.agent_review.all()
        service_provider_profile.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        service_provider_profile.rating = round(total / len(reviews), 2)
        service_provider_profile.save()
        return Response("Review Added")

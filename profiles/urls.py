from django.urls import path

from .views import (ServiceProviderListAPIView, GetProfileAPIView, 
                    UpdateProfileAPIView)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", UpdateProfileAPIView.as_view(), name="update_profile"
    ),
    path("serviceproviders/all/", ServiceProviderListAPIView.as_view(), name="all-agents"),
    
]

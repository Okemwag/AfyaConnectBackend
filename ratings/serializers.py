from rest_framework import serializers

from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    service_provider = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        return obj.rater.username

    def get_service_provider(self, obj):
        return obj.service_provider.user.username

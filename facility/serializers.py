from rest_framework import serializers
from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class FacilityRequestSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    services = serializers.ListField(child=serializers.CharField(), required=False)

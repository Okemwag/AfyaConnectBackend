from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Facility
from .serializers import FacilitySerializer, FacilityRequestSerializer



class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class RecommendFacilityView(APIView):
    def get(self, request):
        serializer = FacilityRequestSerializer(data=request.query_params)
        if serializer.is_valid():
            user_lat = serializer.validated_data['latitude']
            user_lon = serializer.validated_data['longitude']
            required_services = serializer.validated_data.get('services', [])

            user_location = Point(user_lon, user_lat, srid=4326)

            # Filtering facilities based on the required services
            facilities = Facility.objects.all()
            for service in required_services:
                if not hasattr(Facility, service):
                    return Response({"error": f"Invalid service: {service}"}, status=status.HTTP_400_BAD_REQUEST)
                facilities = facilities.exclude(**{service: ''})

            # Calculating distance from user location and sorting by proximity
            facilities = facilities.annotate(distance=Distance('coordinates', user_location)).order_by('distance')

            # Getting the nearest facility
            nearest_facility = facilities.first()

            if not nearest_facility:
                return Response({"message": "No facilities found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)

            
            facility_data = {
                "MFL_Code": nearest_facility.MFL_Code,
                "Facility_Name": nearest_facility.Facility_Name,
                "SubCounty": nearest_facility.SubCounty,
                "Latitude": nearest_facility.Latitude,
                "Longitude": nearest_facility.Longitude,
                "Ward_Name": nearest_facility.ward_name,
                "Level": nearest_facility.Level,
                "Care_and_Treatment_Services": nearest_facility.Care_and_Treatment_Services,
                "HIV_Testing_Services": nearest_facility.HIV_Testing_Services,
                "PrEP_Services": nearest_facility.PrEP_Services,
                "PMTCT_Services": nearest_facility.PMTCT_Services,
                "Distance_km": nearest_facility.distance.km,
            }

            return Response(facility_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





import json
from django.core.management.base import BaseCommand
from facility.models import Facility

class Command(BaseCommand):
    help = 'Load facilities data into PostGIS database'

    def handle(self, *args, **options):
        with open('Healthfacilities.json', 'r') as file:
            facilities_data = json.load(file)

        for facility_data in facilities_data:
            # Check for required keys and handle missing keys
            try:
                facility = Facility.objects.create(
                    MFL_Code=facility_data['MFL_Code'],
                    Facility_Name=facility_data['Facility_Name'],
                    SubCounty=facility_data['SubCounty'],
                    Latitude=float(facility_data['Latitude']),
                    Longitude=float(facility_data['Longitude']),
                    ward_name=facility_data['ward  name'],
                    Level=facility_data['Level'],
                    Care_and_Treatment_Services=facility_data['Care  and  Treatment  Services'],
                    HIV_Testing_Services=facility_data['HIV  Testing  Services'],
                    PrEP_Services=facility_data['PrEP  Services'],
                    PMTCT_Services=facility_data['PMTCT  Services']
                )
                facility.save()
            except KeyError as e:
                missing_key = e.args[0]
                self.stderr.write(self.style.ERROR(f'Missing key {missing_key} in data: {facility_data}'))
                continue

        self.stdout.write(self.style.SUCCESS('Facilities data loaded successfully'))

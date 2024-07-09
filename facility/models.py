from django.contrib.gis.db import models

class Facility(models.Model):
    MFL_Code = models.IntegerField(unique=True, default=0)
    Facility_Name = models.CharField(max_length=255)
    SubCounty = models.CharField(max_length=255,blank=True)
    Latitude = models.FloatField(default=0.0)
    Longitude = models.FloatField(default=0.0)
    ward_name = models.CharField(max_length=255, default='Ward Name')
    Level = models.CharField(max_length=100, default='Level 3')
    Care_and_Treatment_Services = models.CharField(max_length=255, blank=True)
    HIV_Testing_Services = models.CharField(max_length=255, blank=True)
    PrEP_Services = models.CharField(max_length=255, blank=True)
    PMTCT_Services = models.CharField(max_length=255, blank=True)

    coordinates = models.PointField(default='POINT(0.0 0.0)')

    def save(self, *args, **kwargs):
        self.coordinates = f'POINT({self.Longitude} {self.Latitude})'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Facility_Name

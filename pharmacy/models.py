from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    registration = models.CharField(max_length=100, default='Unknown')
    type = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name

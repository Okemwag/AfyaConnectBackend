# Generated by Django 5.0.2 on 2024-05-17 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_rename_name_facility_facility_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='facility_name',
            new_name='Facility_Name',
        ),
    ]

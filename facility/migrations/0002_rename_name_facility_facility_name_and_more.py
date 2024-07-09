# Generated by Django 5.0.2 on 2024-05-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facility',
            old_name='name',
            new_name='facility_name',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='level',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='registration',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='type',
        ),
        migrations.AddField(
            model_name='facility',
            name='Care_and_Treatment_Services',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='HIV_Testing_Services',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='Latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='facility',
            name='Longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='facility',
            name='MFL_Code',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='PMTCT_Services',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='PrEP_Services',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='SubCounty',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='ward_name',
            field=models.CharField(default='Ward Name', max_length=255),
        ),
        migrations.AddField(
            model_name='facility',
            name='Level',
            field=models.CharField(default='Level 3', max_length=100),
        ),
    ]

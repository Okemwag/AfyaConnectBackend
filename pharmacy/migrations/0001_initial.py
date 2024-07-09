# Generated by Django 5.0.2 on 2024-05-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration', models.CharField(default='Unknown', max_length=100)),
                ('type', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
    ]
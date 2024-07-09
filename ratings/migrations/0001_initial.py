# Generated by Django 5.0.2 on 2024-05-13 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facility', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=0, help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent', verbose_name='Rating')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_review', to='facility.facility', verbose_name='Facility being rated')),
                ('rater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User providing the rating')),
            ],
            options={
                'unique_together': {('rater', 'facility')},
            },
        ),
    ]
# Generated by Django 5.0.2 on 2024-05-13 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_options_alter_customuser_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='users_customuser',
        ),
    ]
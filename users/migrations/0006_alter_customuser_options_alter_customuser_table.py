# Generated by Django 5.0.2 on 2024-05-13 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_options_alter_customuser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='users',
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointment_special_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='duration',
            field=models.IntegerField(choices=[(20, '20 minutes'), (30, '30 minutes')], null=True),
        ),
    ]

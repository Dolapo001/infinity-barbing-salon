# Generated by Django 5.0.7 on 2024-08-31 12:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_remove_appointment_style_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='style_sample',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]

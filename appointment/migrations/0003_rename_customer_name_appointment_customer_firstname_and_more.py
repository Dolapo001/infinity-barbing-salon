# Generated by Django 5.0.7 on 2024-07-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_service_alter_appointment_stylist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='customer_name',
            new_name='customer_firstname',
        ),
        migrations.AddField(
            model_name='appointment',
            name='customer_lastname',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='ticket_number',
            field=models.CharField(editable=False, max_length=4, primary_key=True, serialize=False, unique=True),
        ),
    ]

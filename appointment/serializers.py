from rest_framework import serializers
from .models import Appointment


class ScheduleAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'stylist', 'service', 'customer_name', 'customer_email', 'customer_phone']


class RescheduleAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'stylist', 'service']


class CancelAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['ticket_number']


class ConfirmAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['ticket_number']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['feedback']

from datetime import timedelta, datetime

from rest_framework import serializers
from .models import Appointment
import cloudinary.uploader


class ScheduleAppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'stylist', 'service', 'customer_firstname', 'customer_lastname',
                  'customer_email', 'customer_phone', 'special_request', 'style_sample']

    def validate(self, data):
        start_time = data.get('time')
        if start_time:
            start_datetime = datetime.combine(data['date'], start_time)
            duration = 30
            end_time = (start_datetime + timedelta(minutes=duration)).time()
            data['end_time'] = end_time

        return data


class RescheduleAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'stylist', 'service', 'end_time']
        read_only_fields = ['end_time']

    def validate(self, data):
        start_time = data.get('time')
        if start_time:
            start_datetime = datetime.combine(data['date'], start_time)
            duration = 30
            end_time = (start_datetime + timedelta(minutes=duration)).time()
            data['end_time'] = end_time

        return data


class CancelAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['ticket_number']


class ConfirmAppointmentSerializer(serializers.ModelSerializer):
    end_time = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['ticket_number', 'date', 'time', 'end_time', 'stylist', 'service', 'customer_name',
                  'customer_email', 'customer_phone', 'status', 'style_sample']

    def get_end_time(self, obj):
        start_datetime = datetime.combine(obj.date, obj.time)
        duration = 30
        end_datetime = start_datetime + timedelta(minutes=duration)
        return end_datetime.time()

    def get_customer_name(self, obj):
        return f"{obj.customer_firstname} {obj.customer_lastname}"


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['ticket_number']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['feedback']

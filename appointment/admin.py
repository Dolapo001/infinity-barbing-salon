from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'ticket_number', 'date', 'time', 'stylist', 'service',
        'customer_firstname', 'customer_email', 'customer_phone', 'status'
    ]
    search_fields = [
        'id', 'ticket_number', 'customer_firstname', 'customer_email', 'customer_phone', 'stylist', 'service'
    ]
    list_filter = ['date', 'time', 'stylist', 'service', 'status']
    ordering = ['date', 'time', 'stylist']
    fieldsets = (
        (None, {
            'fields': (
                'id', 'ticket_number', 'date', 'time', 'stylist', 'service',
                'customer_firstname', 'customer_email', 'customer_phone', 'status', 'feedback'
            )
        }),
    )
    readonly_fields = ['id', 'ticket_number']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

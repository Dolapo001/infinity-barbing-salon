import logging
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse

logger = logging.getLogger(__name__)


def send_confirmation_email(request, appointment):
    subject = 'Appointment Confirmation'
    sender = settings.DEFAULT_FROM_EMAIL
    recipient = [appointment.customer_email]

    reschedule_url = request.build_absolute_uri(reverse('reschedule-appointment', args=[appointment.ticket_number]))
    cancel_url = request.build_absolute_uri(reverse('cancel-appointment', args=[appointment.ticket_number]))

    context = {
        'customer_firstname': appointment.customer_firstname,
        'stylist': appointment.stylist,
        'date': appointment.date,
        'time': appointment.time,
        'service': appointment.service,
        'ticket_number': appointment.ticket_number,
        'email_sender_name': settings.EMAIL_SENDER_NAME,
        'reschedule_url': reschedule_url,
        'cancel_url': cancel_url,
    }

    email_html_message = render_to_string('appointment_confirmation_email.html', context)
    email_plain_message = render_to_string('confirmation_email.txt', context)

    try:
        msg = EmailMultiAlternatives(subject, email_plain_message, sender, recipient)
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()
        logger.info(f"Email sent successfully to {recipient}")
    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {str(e)}")


def send_status_update_email(request, appointment, status, new_date=None, new_time=None, new_stylist=None):
    subject = f'Appointment {status.capitalize()}'
    sender = settings.DEFAULT_FROM_EMAIL
    recipient = [appointment.customer_email]

    context = {
        'customer_firstname': appointment.customer_firstname,
        'status': status,
        'stylist': new_stylist,
        'service': appointment.service,
        'ticket_number': appointment.ticket_number,
        'email_sender_name': settings.EMAIL_SENDER_NAME,
        'new_date': new_date,
        'new_time': new_time,
    }
    email_html_message = render_to_string('appointment_status_update_email.html', context)
    email_plain_message = render_to_string('status_update_email.txt', context)

    try:
        msg = EmailMultiAlternatives(subject, email_plain_message, sender, recipient)
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()
        logger.info(f"Status update email sent successfully to {recipient}")
    except Exception as e:
        logger.error(f"Failed to send status update email to {recipient}: {str(e)}")


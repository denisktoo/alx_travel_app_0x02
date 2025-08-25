from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation_email(user_email, booking_id, amount):
    subject = "Payment Confirmation"
    message = f"""
    Your payment for Booking #{booking_id} was successful.
    Amount paid: {amount} KES
    Thank you for using our service.
    """
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])

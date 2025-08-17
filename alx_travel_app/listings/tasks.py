from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_payment_confirmation_email(user_email, booking_id, amount):
    subject = "Payment Confirmation"
    message = f"""
    Your payment for Booking #{booking_id} was successful.
    Amount paid: {amount} ETB
    Thank you for using our service.
    """
    send_mail(subject, message, 'no-reply@example.com', [user_email])

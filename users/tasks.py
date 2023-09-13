from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from notebook.celery import app


@app.task
def send_mail(email: str, subject: str, email_html_message: str):
    message = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    message.attach_alternative(email_html_message, "text/html")
    message.send()

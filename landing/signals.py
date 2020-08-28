from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import WantToSee


@receiver(post_save, sender=WantToSee)
def signal_receiver(sender, instance, created, **kwargs):
    if not created:
        return

    email = EmailMessage(
        subject=f"Feedback by {instance.fullname}",
        body=instance.message,
        from_email=settings.ADMIN_EMAIL,
        to=[settings.ADMIN_EMAIL],
        cc=settings.CC_EMAIL_LIST,
        reply_to=[instance.email],
    )
    email.send()

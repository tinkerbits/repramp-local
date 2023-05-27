from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailListRequest
from managers.models import ManagerActions

@receiver(post_save, sender=EmailListRequest)
def create_manager_action(sender, instance, created, **kwargs):
    if created:
        ManagerActions.objects.create(
            action_type='emaillist-approval',
            action_details=instance
        )
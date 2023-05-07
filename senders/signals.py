from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmailList
from managers.models import ManagerActions

@receiver(post_save, sender=EmailList)
def create_manager_action(sender, instance, created, **kwargs):
    if created:
        action = ManagerActions.objects.create(
            action='emaillist-approval',
            action_details=instance
        )
        print("saved this one")

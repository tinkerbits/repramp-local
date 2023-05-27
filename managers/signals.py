from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import ManagerActions
from senders.models import EmailListRequest, EmailListAssignment
from warmuppers.models import EmailAddress

@receiver(pre_save, sender=ManagerActions)
def create_email_list(sender, instance, **kwargs):
    if instance.status == "accepted":
        emaillistrequest_obj = EmailListRequest.objects.get(id=instance.action_details.id)

        gmail_count = emaillistrequest_obj.gmail_count
        random_gmail_addresses = EmailAddress.objects.filter(mailbox_provider='gmail').order_by('?')[:gmail_count]

        google_workspace_count = emaillistrequest_obj.google_workspace_count
        random_google_workspace_addresses = EmailAddress.objects.filter(mailbox_provider='google_workspace').order_by('?')[:google_workspace_count]

        microsoft_count = emaillistrequest_obj.microsoft_count
        random_microsoft_addresses = EmailAddress.objects.filter(mailbox_provider='microsoft').order_by('?')[:microsoft_count]

        msft_365_count = emaillistrequest_obj.msft_365_count
        random_msft365_addresses = EmailAddress.objects.filter(mailbox_provider='msft_365').order_by('?')[:msft_365_count]

        yahoo_count = emaillistrequest_obj.yahoo_count
        random_yahoo_addresses = EmailAddress.objects.filter(mailbox_provider='yahoo').order_by('?')[:yahoo_count]

        other_count = emaillistrequest_obj.other_count
        random_other_addresses = EmailAddress.objects.filter(mailbox_provider='other').order_by('?')[:other_count]

        all_random_addresses = random_gmail_addresses | random_google_workspace_addresses | random_microsoft_addresses | random_msft365_addresses | random_yahoo_addresses | random_other_addresses

        for address in all_random_addresses:
            new_email_address_assignement_obj = EmailListAssignment.objects.create(email_list_request=emaillistrequest_obj, email=address)
            new_email_address_assignement_obj.save()
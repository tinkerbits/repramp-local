from django.db.models import Count
from warmuppers.models import EmailAddress

def get_email_address_count():
    return {
        'gmail_count': EmailAddress.objects.filter(mailbox_provider='gmail', is_active=True).count(),
        'microsoft_count': EmailAddress.objects.filter(mailbox_provider='microsoft', is_active=True).count(),
        'yahoo_count': EmailAddress.objects.filter(mailbox_provider='yahoo', is_active=True).count(),
        'other_count': EmailAddress.objects.filter(mailbox_provider='other', is_active=True).count(),
    }
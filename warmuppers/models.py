from django.db import models
from users.models import CustomUser

class EmailAddress(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email = models.EmailField(unique=True)
    MAILBOX_PROVIDER_CHOICES = (
        ('gmail', 'gmail'),
        ('google_workspace', 'google_workspace'),
        ('microsoft', 'microsoft'),
        ('msft_365', 'msft_365'),
        ('yahoo', 'yahoo'),
        ('other', 'other'),
    )
    mailbox_provider = models.CharField(max_length=20, choices=MAILBOX_PROVIDER_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
class EmailAddressAssignment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE, related_name="email_assignments")
    warmupper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="email_warmuppers")

    def __str__(self):
        return self.email.email
    
class EmailAddressEngagement(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE, related_name="engagement_emails", blank=True, null=True)
    warmupper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="engagement_warmuppers", blank=True, null=True)
    DATA_TYPE_CHOICES = (
        ('open', 'opens'),
        ('click', 'clicks'),
    )
    data_type = models.CharField(max_length=20, choices=DATA_TYPE_CHOICES)    

    def __str__(self):
        return self.email.email

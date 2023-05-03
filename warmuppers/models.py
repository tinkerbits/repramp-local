from django.db import models
from users.models import CustomUser

class EmailAddress(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email = models.EmailField(unique=True)
    MAILBOX_PROVIDER_CHOICES = (
        ('gmail', 'gmail'),
        ('microsoft', 'microsoft'),
        ('yahoo', 'yahoo'),
        ('other', 'other'),
    )
    mailbox_provider = models.CharField(max_length=20, choices=MAILBOX_PROVIDER_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
class Assignment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE, related_name="email_assignments")
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="email_senders")
    warmupper = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="email_warmuppers")

    def __str__(self):
        return self.email

    
from django.db import models
from users.models import CustomUser
from warmuppers.models import EmailAddress
from .utils import get_email_address_count


class EmailListRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender_emaillist_requests")
    name = models.CharField(max_length=100)
    sender_addresses = models.CharField(max_length=1000)
    gmail_count = models.PositiveSmallIntegerField(default=0)
    google_workspace_count = models.PositiveSmallIntegerField(default=0)
    microsoft_count = models.PositiveSmallIntegerField(default=0)
    msft_365_count = models.PositiveSmallIntegerField(default=0)
    yahoo_count = models.PositiveSmallIntegerField(default=0)
    other_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
    
class EmailListAssignment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    email_list_request = models.ForeignKey(EmailListRequest, on_delete=models.CASCADE, related_name="request_list_assignments")
    email = models.ForeignKey(EmailAddress, on_delete=models.CASCADE, related_name="email_list_assignments")

    def __str__(self):
        return self.email.email
    
    

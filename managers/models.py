from django.db import models
from senders.models import EmailList

class ManagerActions(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    action = models.CharField(max_length=100)
    action_details = models.ForeignKey(EmailList, on_delete=models.CASCADE, related_name="action_details", null=True, blank=True)
    STATUS_CHOICES = (
    ('todo', 'todo'),
    ('in_progress', 'in_progress'),
    ('done', 'done'),
    ('rejected', 'rejected'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.action
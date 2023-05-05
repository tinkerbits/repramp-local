    
from django.db import models
from users.models import CustomUser
from .utils import get_email_address_count
from django.core.validators import MaxValueValidator


class EmailList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=100)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sender_emaillists")
    gmail_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(limit_value=get_email_address_count()['gmail_count'])])
    microsoft_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(limit_value=get_email_address_count()['microsoft_count'])])
    yahoo_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(limit_value=get_email_address_count()['yahoo_count'])])
    other_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(limit_value=get_email_address_count()['other_count'])])

    def __str__(self):
        return self.name
    

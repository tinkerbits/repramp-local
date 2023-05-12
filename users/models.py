from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('warmupper', 'warmupper'),
        ('manager', 'manager'),
        ('admin', 'admin'),
        ('sender', 'sender'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    PRIVILEGE_CHOICES = (
        (1, 'bronze'),
        (2, 'silver'),
        (3, 'gold'),
    )

    privilege = models.SmallIntegerField(choices=PRIVILEGE_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.username
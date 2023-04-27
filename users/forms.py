from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model = CustomUser
    fields = UserCreationForm.Meta.fields + ('role',)

class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = UserChangeForm.Meta.fields
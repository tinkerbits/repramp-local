from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role',)

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-solid border-2 p-1 bg-slate-600 text-center w-full'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'border-solid border-2 p-1 bg-slate-600 text-center w-full'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add custom labels to the username and password fields
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
from django import forms
from users.forms import CustomUserCreationForm
from warmuppers.models import EmailAddress
from users.models import CustomUser

class ManageUsersForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'privilege']
        widgets = {
            'role': forms.Select(choices=CustomUser.ROLE_CHOICES),
            'privilege': forms.Select(choices=CustomUser.PRIVILEGE_CHOICES),
        }


class RegisterNewUserForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            ('warmupper', 'warmupper'),
            ('sender', 'sender'),
        ]

class AddEmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email', 'mailbox_provider']

class UploadEmailAddressesForm(forms.Form):
    file = forms.FileField()

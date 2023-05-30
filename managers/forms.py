from django import forms
from users.forms import CustomUserCreationForm
from warmuppers.models import EmailAddress, EmailAddressEngagement
from users.models import CustomUser

class ManageSomeUsersForm(forms.ModelForm):

    ROLE_CHOICES = (
        ('sender', 'sender'),
        ('warmupper', 'warmupper'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'privilege']
        widgets = {
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

class UploadEngagementDataForm(forms.ModelForm):

    file = forms.FileField()

    class Meta:
        model = EmailAddressEngagement
        fields = ['data_type', 'file']


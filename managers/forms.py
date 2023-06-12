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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600'

class RegisterNewUserForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            ('sender', 'sender'),
            ('warmupper', 'warmupper'),
        ]
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600 text-center w-full'
            field.widget.attrs['placeholder'] = field.label

class AddEmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email', 'mailbox_provider']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600 text-center w-full'

class UploadEmailAddressesForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600 text-center w-full'
            field.widget.attrs['initial'] = ''

class UploadEngagementDataForm(forms.ModelForm):

    file = forms.FileField()

    class Meta:
        model = EmailAddressEngagement
        fields = ['data_type', 'file']


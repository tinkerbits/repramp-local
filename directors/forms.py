from django import forms
from users.models import CustomUser


class ManageAllUsersForm(forms.ModelForm):

    ROLE_CHOICES = (
        ('warmupper', 'warmupper'),
        ('sender', 'sender'),
        ('manager', 'manager'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'privilege']
        widgets = {
            'privilege': forms.Select(choices=CustomUser.PRIVILEGE_CHOICES),
        }
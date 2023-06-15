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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600'
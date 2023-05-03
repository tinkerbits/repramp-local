from users.forms import CustomUserCreationForm

class RegisterNewUserForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            ('warmupper', 'warmupper'),
            ('sender', 'sender'),
        ]
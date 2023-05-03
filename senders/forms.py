from django import forms
from .models import EmailList


class EmailListCreationForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = ('name','gmail_count', 'microsoft_count', 'yahoo_count', 'other_count',)


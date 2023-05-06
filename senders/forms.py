from django import forms
from .models import EmailList
from .utils import get_email_address_count
from django.core.validators import MaxValueValidator



class EmailListCreationForm(forms.ModelForm):
    class Meta:
        model = EmailList
        fields = ('name', 'gmail_count', 'microsoft_count', 'yahoo_count', 'other_count',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email_counts = get_email_address_count()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_gmail_count(self):
        gmail_count = self.cleaned_data['gmail_count']
        if gmail_count > self.email_counts['gmail_count']:
            raise forms.ValidationError("Gmail is full")
        return gmail_count

    def clean_microsoft_count(self):
        microsoft_count = self.cleaned_data['microsoft_count']
        if microsoft_count > self.email_counts['microsoft_count']:
            raise forms.ValidationError("Microsoft is full")
        return microsoft_count

    def clean_yahoo_count(self):
        yahoo_count = self.cleaned_data['yahoo_count']
        if yahoo_count > self.email_counts['yahoo_count']:
            raise forms.ValidationError("Yahoo is full")
        return yahoo_count

    def clean_other_count(self):
        other_count = self.cleaned_data['other_count']
        if other_count > self.email_counts['other_count']:
            raise forms.ValidationError("Other is full")
        return other_count


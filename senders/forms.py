from django import forms
from .models import EmailListRequest
from .utils import get_email_address_count
from django.core.validators import MaxValueValidator



class EmailListCreationForm(forms.ModelForm):
    class Meta:
        model = EmailListRequest
        fields = ('name', 'sender_addresses', 'gmail_count', 'google_workspace_count', 'microsoft_count', 'msft_365_count', 'yahoo_count', 'other_count',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email_counts = get_email_address_count()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-solid border-2 p-1 bg-slate-600 w-full'

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def clean_gmail_count(self):
        gmail_count = self.cleaned_data['gmail_count']
        if gmail_count > self.email_counts['gmail_count']:
            raise forms.ValidationError("Insufficient Gmail addresses available.")
        return gmail_count

    def clean_google_workspace_count(self):
        google_workspace_count = self.cleaned_data['google_workspace_count']
        if google_workspace_count > self.email_counts['google_workspace_count']:
            raise forms.ValidationError("Insufficient Google Workspace addresses available.")
        return google_workspace_count

    def clean_microsoft_count(self):
        microsoft_count = self.cleaned_data['microsoft_count']
        if microsoft_count > self.email_counts['microsoft_count']:
            raise forms.ValidationError("Insufficient Microsoft addresses available.")
        return microsoft_count
    
    def clean_msft_365_count(self):
        msft_365_count = self.cleaned_data['msft_365_count']
        if msft_365_count > self.email_counts['msft_365_count']:
            raise forms.ValidationError("Insufficient Microsoft 365 addresses available.")
        return msft_365_count

    def clean_yahoo_count(self):
        yahoo_count = self.cleaned_data['yahoo_count']
        if yahoo_count > self.email_counts['yahoo_count']:
            raise forms.ValidationError("Insufficient Yahoo addresses available.")
        return yahoo_count

    def clean_other_count(self):
        other_count = self.cleaned_data['other_count']
        if other_count > self.email_counts['other_count']:
            raise forms.ValidationError("Insufficient Other addresses available.")
        return other_count


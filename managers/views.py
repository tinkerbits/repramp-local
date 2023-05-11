import csv
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect


from .forms import RegisterNewUserForm, AddEmailAddressForm, UploadEmailAddressesForm
from warmuppers.models import EmailAddress


class RegisterNewWarmupperView(CreateView):
    form_class = RegisterNewUserForm
    success_url = reverse_lazy('gateway')
    template_name = 'managers/register-new-warmupper.html'

class AssignEmailAddressesToWarmupperView(TemplateView):
    template_name = 'managers/assign-email-addresses-to-warmupper.html'

class CalculateWarmupperEmailEngagementView(TemplateView):
    template_name = 'managers/calculate-warmupper-email-engagement.html'

class WarmupperEmailEngagementAndRenumeration(TemplateView):
    template_name = 'managers/warmupper-email-engagement-and-renumeration.html'

class AddEmailAddresses(CreateView):
    template_name = 'managers/add-email-addresses.html'
    success_url = reverse_lazy('gateway')
    form_class = AddEmailAddressForm
    second_form_class = UploadEmailAddressesForm

    # Adds the second_form_flass to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["upload_email_form"] = self.second_form_class()
        return context
    
    # Intercepts the form data from both forms and then validates it with form.is_valid()
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        upload_form = self.second_form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        if upload_form.is_valid():
            ###process uploaded csv
            uploaded_file = upload_form.cleaned_data['file']
            reader = csv.reader(uploaded_file.read().decode('utf-8').splitlines())

            for row in reader:
                obj = EmailAddress(email=row[0], mailbox_provider=row[1])
                obj.save()
        

        return HttpResponseRedirect(self.success_url)

    



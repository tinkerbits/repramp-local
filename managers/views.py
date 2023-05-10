from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponseRedirect


from .forms import RegisterNewUserForm, AddEmailAddressForm, UploadEmailAddressesForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["upload_email_form"] = self.second_form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        upload_form = self.second_form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        if upload_form.is_valid():
            upload_form.save()

        return HttpResponseRedirect(self.success_url)

    



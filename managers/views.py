from django.urls import reverse_lazy

from django.views.generic import CreateView, TemplateView

from users.forms import CustomUserCreationForm


class RegisterNewWarmupperView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('gateway')
    template_name = 'managers/register-new-warmupper.html'

class AssignEmailAddressesToWarmupperView(TemplateView):
    template_name = 'managers/assign-email-addresses-to-warmupper.html'

class CalculateWarmupperEmailEngagementView(TemplateView):
    template_name = 'managers/calculate-warmupper-email-engagement.html'

class WarmupperEmailEngagementAndRenumeration(TemplateView):
    template_name = 'managers/warmupper-email-engagement-and-renumeration.html'


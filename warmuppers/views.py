from django.views.generic import TemplateView
from .models import EmailAddressAssignment


class AssignedEmailAddressesView(TemplateView):
    template_name = 'warmuppers/assigned-email-addresses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["this_users_email_address_assignments"] =  EmailAddressAssignment.objects.filter(warmupper=self.request.user.id)
        return context
    
class EmailEngagementAndRenumerationView(TemplateView):
    template_name = 'warmuppers/email-engagement-and-renumeration.html'

from django.views.generic import TemplateView


class AssignedEmailAddressesView(TemplateView):
    template_name = 'warmuppers/assigned-email-addresses.html'


class EmailEngagementAndRenumerationView(TemplateView):
    template_name = 'warmuppers/email-engagement-and-renumeration.html'

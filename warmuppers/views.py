from django.views.generic import TemplateView


class AssignedEmailAddressesView(TemplateView):
    template_name = 'w-assigned-email-addresses.html'


class EmailEngagementAndRenumerationView(TemplateView):
    template_name = 'w-email-engagement-and-renumeration.html'

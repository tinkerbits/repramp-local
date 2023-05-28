from django.views.generic import TemplateView
from .models import EmailAddressAssignment
from senders.models import EmailListAssignment


class AssignedEmailAddressesView(TemplateView):
    template_name = 'warmuppers/assigned-email-addresses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # User's Assigned Email Addresses

        this_users_email_address_assignments = EmailAddressAssignment.objects.filter(warmupper=self.request.user.id)

        context["this_users_email_address_assignments"] =  this_users_email_address_assignments


        # Sender Address Search String

        email_address_ids = [assignment.email.id for assignment in this_users_email_address_assignments]
        email_addresses_assigned_to_list_requests = EmailListAssignment.objects.filter(email_id__in=email_address_ids)

        senderaddresslist = []

        for email_address_assignment in email_addresses_assigned_to_list_requests:
            senderaddressstring = email_address_assignment.email_list_request.sender_addresses
            senderaddresses = senderaddressstring.split(";")

            for senderaddress in senderaddresses:
                senderaddress = 'from:' + senderaddress
                if senderaddress not in senderaddresslist:
                    senderaddresslist.append(senderaddress)

        context["senderaddresses"] = ' OR '.join(senderaddresslist)

        return context
    
class EmailEngagementAndRenumerationView(TemplateView):
    template_name = 'warmuppers/email-engagement-and-renumeration.html'

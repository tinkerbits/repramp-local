import csv

from django.views import View
from django.views.generic import CreateView, TemplateView
from .forms import EmailListCreationForm
from django.urls import reverse_lazy
from .utils import get_email_address_count
from django.http import HttpResponse, FileResponse


from managers.models import ManagerActions
from senders.models import EmailListAssignment



class CreateNewEmailListView(CreateView):
    template_name = 'senders/create-new-email-list-request.html'
    form_class = EmailListCreationForm
    success_url = reverse_lazy('gateway')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email_counts'] = get_email_address_count()
        return context

    def form_valid(self, form):

        form.instance.sender = self.request.user

        addresses = form.cleaned_data['sender_addresses'].split(';')
        form.instance.sender_addresses = ';'.join([address.strip() for address in addresses])

        return super().form_valid(form)
    
class ManageEmailListsView(TemplateView):

    template_name = 'senders/manage-email-lists.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        requested_email_lists = ManagerActions.objects.filter(
            action_type='emaillist-approval', 
            action_details__sender=self.request.user
            )
        context['email_list_requests'] = requested_email_lists

        email_list_assignments = EmailListAssignment.objects.filter(
            email_list_request__sender=self.request.user
        )
        context['email_list_assignments'] = email_list_assignments

        return context
    
class DownloadEmailListAssignmentsView(View):
    def get(self, request, *args, **kwargs):
        
        emaillistassignments = EmailListAssignment.objects.filter(email_list_request__sender=self.request.user, email_list_request__id=kwargs['id'])
        firstassignment = emaillistassignments.first()
        email_list_request_name = firstassignment.email_list_request.name


        response = HttpResponse(content_type='text/csv', headers={'Content-Disposition': f'attachment; filename="{email_list_request_name}_email_list.csv"'})

        writer = csv.writer(response)

        for email_list_assignment in emaillistassignments:
            writer.writerow([email_list_assignment.email.email])

        return response



    
    

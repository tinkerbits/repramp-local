from django.views.generic import CreateView, TemplateView
from .forms import EmailListCreationForm
from django.urls import reverse_lazy
from .utils import get_email_address_count

from managers.models import ManagerActions



class CreateNewEmailListView(CreateView):
    template_name = 'senders/create-new-email-list.html'
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
        accepted_actions = ManagerActions.objects.filter(
            action_type='emaillist-approval', 
            status='accepted',
            action_details__sender=self.request.user
            )

        context['email_lists'] = accepted_actions

        return context
    
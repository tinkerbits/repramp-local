from django.views.generic import CreateView
from .forms import EmailListCreationForm
from django.urls import reverse_lazy
from users.models import CustomUser



class CreateEmailListView(CreateView):
    template_name = 'senders/create-email-list.html'
    form_class = EmailListCreationForm
    success_url = reverse_lazy('gateway')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
    
    

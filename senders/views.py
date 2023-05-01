from django.views.generic import TemplateView


class CreateEmailListView(TemplateView):
    template_name = 'senders/create-email-list.html'

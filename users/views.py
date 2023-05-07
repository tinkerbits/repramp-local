from django.views.generic import TemplateView

from senders.models import EmailList

class GatewayView(TemplateView):
    template_name = 'gateway.html'
    model = EmailList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["this_users_email_lists"] =  EmailList.objects.filter(sender=self.request.user.id)
        context["pending_email_lists"] = EmailList.objects.filter()
        return context

    




import logging

from django.views.generic import TemplateView

from senders.models import EmailList
from managers.models import ManagerActions

class GatewayView(TemplateView):
    template_name = 'gateway.html'
    model = EmailList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["this_users_email_lists"] =  EmailList.objects.filter(sender=self.request.user.id)
        context["manager_actions"] = ManagerActions.objects.all()
        return context

    def get(self,request, *args, **kwargs):
        query = request.GET.get('m1-actionid')

        if query and request.GET.get('m1-comment'):
            obj = ManagerActions.objects.get(id=query)
            obj.comment = request.GET.get('m1-comment')
            obj.save()
            return super().get(request, *args, **kwargs)
            
        elif query and request.GET.get('m1-status'):
            
            if request.GET.get('m1-status') == 'empty':
                obj = ManagerActions.objects.get(id=query)
                obj.status = None
                obj.save()
                return super().get(request, *args, **kwargs)
            else:
                obj = ManagerActions.objects.get(id=query)
                obj.status = request.GET.get('m1-status')
                obj.save()
                return super().get(request, *args, **kwargs)

        else:
            return super().get(request, *args, **kwargs)


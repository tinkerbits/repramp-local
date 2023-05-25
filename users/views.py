from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.views.generic import TemplateView
from django.db.models import Sum, Case, When

from warmuppers.models import EmailAddressEngagement
from senders.models import EmailList
from managers.models import ManagerActions

class GatewayView(TemplateView):
    template_name = 'gateway.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["this_users_email_lists"] =  EmailList.objects.filter(sender=self.request.user.id)

        context["manager_actions"] = ManagerActions.objects.all()

        last_month = datetime.now() - relativedelta(months=1)


        context["engagement_by_warmupper"] = EmailAddressEngagement.objects.filter(created__gte=last_month).select_related(
                'warmupper'
            ).values(
                'warmupper__username'
            ).annotate(
                opens_sum=Sum(Case(When(data_type='open', then=1), default=0)),
                clicks_sum=Sum(Case(When(data_type='click', then=1), default=0))
            ).order_by('warmupper__username')
        
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


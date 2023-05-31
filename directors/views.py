from django.db.models import Q
from django.views.generic import ListView
from users.models import CustomUser

from .forms import ManageAllUsersForm


class ManageAllUsersView(ListView):
    template_name = 'directors/manage-all-users.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_forms = []
        warmuppers_or_senders_or_managers = CustomUser.objects.filter(Q(role="warmupper") | Q(role="sender") | Q(role="manager"))
        for user in warmuppers_or_senders_or_managers:
            user_form = ManageAllUsersForm(instance=user)
            user_forms.append(user_form)
        context['user_forms'] = user_forms

        return context
    
    def get(self,request, *args, **kwargs):
        userid = request.GET.get('d1-userid')
        username = request.GET.get('d1-username')
        email = request.GET.get('d1-email')
        first_name = request.GET.get('d1-first_name')
        last_name = request.GET.get('d1-last_name')
        role = request.GET.get('d1-role')
        privilege = request.GET.get('d1-privilege')

        if userid:
            obj = CustomUser.objects.get(id=userid)
            obj.username = username
            obj.email = email
            obj.first_name = first_name
            obj.last_name = last_name
            obj.role = role
            if role == 'sender' and privilege:
                obj.privilege = privilege
            else:
                obj.privilege = None
            obj.save()
            return super().get(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)
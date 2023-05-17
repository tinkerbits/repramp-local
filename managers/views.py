import csv

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponseRedirect
from django.db.models import Q

from .forms import ManageUsersForm, RegisterNewUserForm, AddEmailAddressForm, UploadEmailAddressesForm
from warmuppers.models import EmailAddress, EmailAddressAssignment
from users.models import CustomUser


class ManageUsersView(ListView):
    template_name = 'managers/manage-users.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_forms = []
        warmuppers_or_senders = CustomUser.objects.filter(Q(role="warmupper") | Q(role="sender"))
        for user in warmuppers_or_senders:
            user_form = ManageUsersForm(instance=user)
            user_forms.append(user_form)
        context['user_forms'] = user_forms

        return context
    
    def get(self,request, *args, **kwargs):
        userid = request.GET.get('m2-userid')
        username = request.GET.get('m2-username')
        email = request.GET.get('m2-email')
        first_name = request.GET.get('m2-first_name')
        last_name = request.GET.get('m2-last_name')
        role = request.GET.get('m2-role')
        privilege = request.GET.get('m2-privilege')

        if userid:
            obj = CustomUser.objects.get(id=userid)
            obj.username = username
            obj.email = email
            obj.first_name = first_name
            obj.last_name = last_name
            obj.role = role
            if privilege:
                obj.privilege = privilege
            obj.save()
            return super().get(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)


class RegisterNewUserView(CreateView):
    template_name = 'managers/register-new-user.html'
    form_class = RegisterNewUserForm
    success_url = reverse_lazy('gateway')

class AssignEmailAddressesToWarmupperView(ListView):
    template_name = 'managers/assign-email-addresses-to-warmupper.html'
    model = EmailAddress

    def post(self, request, *args, **kwargs):
        
        for key, value in request.POST.items():
            if key != 'null':
                emailobj = EmailAddress.objects.get(id=key)
                warmupperobj = CustomUser.objects.get(id=value)
                assignmentqs = EmailAddressAssignment.objects.filter(email=emailobj)

                if assignmentqs.exists():
                    for assignmentobj in assignmentqs:
                        if assignmentobj.warmupper == warmupperobj:
                            continue
                        else:
                            assignmentobj.warmupper = warmupperobj
                            assignmentobj.save()
                else:
                    newassignmentobj = EmailAddressAssignment(email=emailobj, warmupper=warmupperobj)
                    newassignmentobj.save()

        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        warmuppers = CustomUser.objects.filter(role="warmupper")
        context['warmupper_list'] = warmuppers

        emailaddressassignments = EmailAddressAssignment.objects.all()
        context['emailaddressassignment_list'] = emailaddressassignments
        return context

class CalculateWarmupperEmailEngagementView(TemplateView):
    template_name = 'managers/calculate-warmupper-email-engagement.html'

class WarmupperEmailEngagementAndRenumeration(TemplateView):
    template_name = 'managers/warmupper-email-engagement-and-renumeration.html'

class AddEmailAddresses(CreateView):
    template_name = 'managers/add-email-addresses.html'
    success_url = reverse_lazy('gateway')
    form_class = AddEmailAddressForm
    second_form_class = UploadEmailAddressesForm

    # Adds the second_form_flass to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["upload_email_form"] = self.second_form_class()
        return context
    
    # Intercepts the form data from both forms and then validates it with form.is_valid()
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        upload_form = self.second_form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        if upload_form.is_valid():
            ###process uploaded csv
            uploaded_file = upload_form.cleaned_data['file']
            reader = csv.reader(uploaded_file.read().decode('utf-8').splitlines())

            for row in reader:
                obj = EmailAddress(email=row[0], mailbox_provider=row[1])
                obj.save()
        

        return HttpResponseRedirect(self.success_url)

    



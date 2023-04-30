from django.urls import path

from .views import AssignedEmailAddressesView, EmailEngagementAndRenumerationView

urlpatterns = [
    path('assigned-email-addresses/', AssignedEmailAddressesView.as_view(), name='w-assigned-email-addresses'),
    path('email-engagement-and-renumeration/', EmailEngagementAndRenumerationView.as_view(), name='w-email-engagement-and-renumeration'),
]

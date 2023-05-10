from django.urls import path

from .views import RegisterNewWarmupperView, AssignEmailAddressesToWarmupperView, CalculateWarmupperEmailEngagementView, WarmupperEmailEngagementAndRenumeration, AddEmailAddresses



urlpatterns = [
    path('register-new-user/', RegisterNewWarmupperView.as_view(), name='m-register-new-user'),
    path('assign-email-addresses-to-warmupper/', AssignEmailAddressesToWarmupperView.as_view(), name='m-assign-email-addresses-to-warmupper'),
    path('calculate-warmupper-email-engagement/', CalculateWarmupperEmailEngagementView.as_view(), name='m-calculate-warmupper-email-engagement'),
    path('warmupper-email-engagement-and-renumeration/', WarmupperEmailEngagementAndRenumeration.as_view(), name='m-warmupper-email-engagement-and-renumeration'),
    path('add-email-addresses/', AddEmailAddresses.as_view(), name='m-add-email-addresses')
]
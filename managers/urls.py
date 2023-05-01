from django.urls import path

from .views import RegisterNewWarmupperView, AssignEmailAddressesToWarmupperView, CalculateWarmupperEmailEngagementView, WarmupperEmailEngagementAndRenumeration



urlpatterns = [
    path('register-new-warmupper/', RegisterNewWarmupperView.as_view(), name='m-register-new-warmupper'),
    path('assign-email-addresses-to-warmupper/', AssignEmailAddressesToWarmupperView.as_view(), name='m-assign-email-addresses-to-warmupper'),
    path('calculate-warmupper-email-engagement/', CalculateWarmupperEmailEngagementView.as_view(), name='m-calculate-warmupper-email-engagement'),
    path('warmupper-email-engagement-and-renumeration/', WarmupperEmailEngagementAndRenumeration.as_view(), name='m-warmupper-email-engagement-and-renumeration')
]
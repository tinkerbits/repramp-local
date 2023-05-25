from django.urls import path

from .views import ManageUsersView, ManageEmailAddresses, CalculateWarmupperEmailEngagementView, WarmupperEmailEngagementAndRenumeration, AddNewEmailAddresses, RegisterNewUserView



urlpatterns = [
    path('manage-users/', ManageUsersView.as_view(), name='m-manage-users'),
    path('register-new-user/', RegisterNewUserView.as_view(), name='m-register-new-user'),
    path('manage-email-addresses/', ManageEmailAddresses.as_view(), name='m-manage-email-addresses'),
    path('add-new-email-addresses/', AddNewEmailAddresses.as_view(), name='m-add-new-email-addresses'),
    path('calculate-warmupper-email-engagement/', CalculateWarmupperEmailEngagementView.as_view(), name='m-calculate-warmupper-email-engagement'),
    path('warmupper-email-engagement-and-renumeration/', WarmupperEmailEngagementAndRenumeration.as_view(), name='m-warmupper-email-engagement-and-renumeration')
]
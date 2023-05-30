from django.urls import path

from .views import ManageAllUsersView


urlpatterns = [
    path('manage-all-users/', ManageAllUsersView.as_view(), name='d-manage-all-users'),
]
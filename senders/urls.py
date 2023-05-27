from django.urls import path

from .views import CreateNewEmailListView, ManageEmailListsView

urlpatterns = [
    path('create-email-list/', CreateNewEmailListView.as_view(), name='s-create-new-email-list'),
    path('manage-email-lists/', ManageEmailListsView.as_view(), name='s-manage-email-lists'),

]

from django.urls import path

from .views import CreateEmailListView, ManageEmailListsView

urlpatterns = [
    path('create-email-list/', CreateEmailListView.as_view(), name='s-create-email-list'),
    path('manage-email-lists/', ManageEmailListsView.as_view(), name='s-manage-email-lists'),

]

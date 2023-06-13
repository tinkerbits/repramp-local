from django.urls import path

from .views import CreateNewEmailListView, ManageEmailListsView, DownloadEmailListAssignmentsView

urlpatterns = [
    path('create-new-email-list-request/', CreateNewEmailListView.as_view(), name='s-create-new-email-list-request'),
    path('manage-email-lists/', ManageEmailListsView.as_view(), name='s-manage-email-lists'),
    path('manage-email-lists/download/<int:id>/', DownloadEmailListAssignmentsView.as_view(), name='download_email_list_assignments'),
]

from django.urls import path

from .views import CreateEmailListView

urlpatterns = [
    path('create-email-list/', CreateEmailListView.as_view(), name='s-create-email-list'),
]

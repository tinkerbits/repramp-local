from django.urls import path

from .views import GatewayView


urlpatterns = [
    path('', GatewayView.as_view(), name='gateway'),
]
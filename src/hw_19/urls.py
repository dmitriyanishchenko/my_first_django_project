from django.urls import path
from .views import air_ticket

urlpatterns = [
    path('air/', air_ticket, name='air_ticket'),
]
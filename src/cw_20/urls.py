from django.urls import path
from .views import (
    home,
    create_customer,
    edit_customer,
    remove_customer,
)

urlpatterns = [
    path('home/', home, name='home'),
    path('add/', create_customer, name='create_customer'),
    path('edit/<int:customer_id>', edit_customer, name='edit_customer'),
    path('remove/<int:customer_id>', remove_customer, name='remove_customer'),
]
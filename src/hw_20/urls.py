from django.urls import path
from .views import (
    home,
    create_car,
    edit_car,
    remove_car,
)

urlpatterns = [
    path('home/', home, name='home'),
    path('add/', create_car, name='create_car'),
    path('edit/<int:car_id>', edit_car, name='edit_car'),
    path('remove/<int:car_id>', remove_car, name='remove_car'),
]
from django.shortcuts import redirect
from hw_20.models import Car


def remove_car(request, car_id):
    car = Car.objects.get(id=car_id)
    print(f'{car.brand} has been removed')
    car.delete()
    return redirect('home')

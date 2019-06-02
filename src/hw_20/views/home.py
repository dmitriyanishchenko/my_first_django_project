from django.shortcuts import render, redirect
from hw_20.models import Car


def home(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'home_car.html', context)

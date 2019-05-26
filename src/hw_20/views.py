from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
# from .models import Car
from .forms import CarForm
from .models import Car


def home(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'home_car.html', context)


def create_car(request):
    if request.method == 'GET':
        context = {'form': CarForm()}
        return render(request, 'add_car.html', context)
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand')
            model = data.get('model')
            color = data.get('color')
            weight = data.get('weight')
            fullname = data.get('fullname')
            year = data.get('year')
            Car.objects.create(
                brand=brand,
                model=model,
                color=color,
                weight=weight,
                fullname=fullname,
                year=year,
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'GET':
        context = {
            'car_id': car_id,
            'form': CarForm(
                initial={
                    'brand': car.brand,
                    'model': car.model,
                    'color': car.color,
                    'weight': car.weight,
                    'fullname': car.fullname,
                    'year': car.year,
                },
            ),
        }
        return render(request, 'edit_car.html', context)
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Car.objects.filter(id=car_id).update(
                brand=data.get('brand'),
                model=data.get('model'),
                color=data.get('color'),
                weight=data.get('weight'),
                fullname=data.get('fullname'),
                year=data.get('year'),
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def remove_car(request, car_id):
    car = Car.objects.get(id=car_id)
    print(f'{car.brand} has been removed')
    car.delete()
    return redirect('home')

from django.shortcuts import render, redirect
from hw_20.models import Car
from hw_20.forms import CarForm
from django.http import HttpResponse


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

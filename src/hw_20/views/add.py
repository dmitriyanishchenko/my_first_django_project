from django.shortcuts import render, redirect
from hw_20.models import Car
from hw_20.forms import CarForm
from django.http import HttpResponse


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

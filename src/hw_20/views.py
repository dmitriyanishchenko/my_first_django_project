from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
from .models import Car
from .forms import CarForm


def home(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'home.html', context)


def create_car(request):
    if request.method == 'GET':
        context = {'form': CarForm()}
        return render(request, 'add.html', context)
    elif request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand') # todo
            lastname = data.get('lastname')
            age = data.get('age')
            profession = data.get('profession')
            Customer.objects.create(
                firstname=firstname,
                lastname=lastname,
                age=age,
                profession=profession,
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def edit_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.method == 'GET':
        context = {
            'customer_id': customer_id,
            'form': CustomerForm(
                initial={
                    'firstname': customer.firstname,
                    'lastname': customer.lastname,
                    'age': customer.age,
                    'profession': customer.profession,
                },
            ),
        }
        return render(request, 'edit.html', context)
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Customer.objects.filter(id=customer_id).update(
                firstname=data.get('firstname'),
                lastname=data.get('lastname'),
                age=data.get('age'),
                profession=data.get('profession'),
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def remove_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    print(f'{customer.firstname} has been removed')
    customer.delete()
    return redirect('home')

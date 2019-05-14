from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse('len is {}'.format(len(name)))
    return HttpResponse('It is Get request')


def index2(request):
    age = request.POST.get('age')
    age = int(age)
    if age < 18:
        return HttpResponse('В доступе отказано')
    return HttpResponse('Добро пожаловать')

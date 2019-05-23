from django.shortcuts import render
from django.http import HttpResponse
from hw_19.forms import PostForm
from django.template import loader


def air_ticket(request):
    """
    Содать форму через django forms, описывающую форму заказа авиабилета.
    форма должна содержать следующие поля - имя, откуда, куда, сколько человек, дата.
    При отправке данных пользователем проверять валидность данных, если они валидны и
    количество человек равно 1, то вывести результат - "стоимость 100 $", если количество
    человек больше 1, то стоимость должна считаться по формуле 100*2*количество человек.
    Если данные не валидны, то вывести ошибку.

    """
    if request.method == 'GET':
        form = PostForm()
        context = {'form': form}
        return render(request, 'air_ticket.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            city_from = data.get('city_from')
            city_to = data.get('city_to')
            number = data.get('number')
            date = data.get('date')
            if number == 1:
                cost = 100
            elif number > 1:
                cost = number * 2 * 100
            return render(request, 'display1_line.html', {'name': name, 'city_from': city_from, 'number': number,
                                                              'city_to': city_to, 'date': date, 'cost': cost})
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

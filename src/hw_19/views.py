from django.shortcuts import render
from django.http import HttpResponse
from hw_19.forms import PostForm
from django.template import loader


def air_ticket(request):
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
                template = loader.get_template('display1_line.html')
                return HttpResponse(template.render({'name': name, 'city_from': city_from, 'number': number,
                                                     'city_to': city_to, 'date': date, 'cost': cost}, request))

            elif number > 1:
                cost = number * 2 * 100
                template = loader.get_template('display1_line.html')
                return HttpResponse(template.render({'name': name, 'city_from': city_from, 'number': number,
                                                     'city_to': city_to, 'date': date, 'cost': cost}, request))
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

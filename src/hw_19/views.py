from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from hw_19.forms import PostForm


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
            print(f'{name}|{city_from}|{city_to}|{number}|{date}')
            context = {'form': form}
            return render(request, 'air_ticket.html', context)
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

# Create your views here.

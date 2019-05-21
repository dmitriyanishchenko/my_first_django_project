from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from cw_19.forms import PostForm

def comment_add(request):
    if request.method == 'GET':
        return render(request, 'comment_add.html')
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            print(f'{firstname}|{lastname}|{age}|{comment}')
            return render(request, 'comment_add.html')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')

# Create your views here.

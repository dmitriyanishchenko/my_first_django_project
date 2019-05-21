from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def comment_add(request):
    if request.method == 'GET':
        return render(request, 'comment_add.html')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        print(f'{firstname}|{lastname}|{age}|{comment}')
        return render(request, 'comment_add.html')
    return HttpResponse('Wrong request method')

# Create your views here.

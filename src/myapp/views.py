from django.shortcuts import render
from django.http import HttpResponse
def index(request):
   if request.method == 'POST':

      name = request.POST.get('name')
      return HttpResponse('len is {}' .format(len(name)))
   return HttpResponse('It is Get request')

from django.shortcuts import render
from django.http import HttpResponse


def line_to_file(request):
    """
    Создать форму из трех полей: имя, фамилия, возраст.
    Создать представление (view. В случае GET запроса отображать форму.
    В случае POST запроса записывать все три поля в виде одной строки в файл
    и после  отображать форму

    """
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        result_string = f' Name is {name}, surname is {surname}, age is {age}'
        with open('test.txt', 'w') as my_file:
            my_file.write('result_string')
            my_file.close()
        return HttpResponse(result_string)




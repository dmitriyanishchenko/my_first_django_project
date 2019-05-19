from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def line_to_file(request):
    """
    Создать форму из трех полей: имя, фамилия, возраст.
    Создать представление (view. В случае GET запроса отображать форму.
    В случае POST запроса записывать все три поля в виде одной строки в файл
    и после  отображать форму

    """
    if request.method == "GET":
        template = loader.get_template('form_line.html')
        return HttpResponse(template.render({}, request))
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        result_string = f'{name},{surname},{age}'
        with open('test_18_2.txt', 'w') as my_file:
            my_file.write(result_string + '\n')
        my_file.close()
        template = loader.get_template('form_line.html')
        return HttpResponse(template.render({}, request))


def file_to_list(request):
    """
    Создать форму, принимающую на вход список и отображающая его.
    Создать представление. В случае GET запроса считать все строки файла в список.
    Произвести рендиринг шаблона и данных (списка строк) и после вернуть пользователю.

    """
    if request.method == "GET":
        with open('test_18_2.txt', 'r') as my_file:
            file_string = my_file.readline()
        res_split = file_string.split(',')
        name = res_split[0]
        surname = res_split[1]
        age = res_split[2]
        template = loader.get_template('display_line.html')
        return HttpResponse(template.render({'name': name, 'surname': surname, 'age': age}, request))



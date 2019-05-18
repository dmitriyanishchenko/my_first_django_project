from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def comment_count(request):
    """
    Дана форма, содержащая  следующие поля: Имя, фамилия, комментарий.
    Вывести пользователю длину комментария, количество гласных и согласных букв в комментарии.

    """
    if request.method == "POST":
        comment = list(request.POST.get('comment'))
        len_com = len(comment)
        vowels = 'eyuioaj'
        consonant = 'qwrtpsdfghklzxcvbnm'
        count_cons = 0
        count_vow = 0
        for elem in comment:
            if elem in vowels:
                count_vow += 1
            elif elem in consonant:
                count_cons += 1
        result = f'Длина комментария {len_com} зн., гласных {count_vow}, согласных {count_cons}'
        return HttpResponse(result)
    return HttpResponse('It is GET request')


def string_cut(request):
    """
    Дана форма, содержащая следующие поля: имя, возраст, комментарий.
    Вывести комментарий пользователя, разделённый на строки.
    Каждую строку дополнить в конце следующей надписью: "(с) {имя автора}"

    """
    if request.method == "POST":
        comment = request.POST.get('comment')
        author = request.POST.get('name')
        add_string = f'(c) {author}'
        res_split = comment.split('\n')
        result = []
        for i in range(len(res_split)):
            elem = res_split[i]
            result.append(elem + add_string)
        my_result = '<br>'.join(result)
        return HttpResponse(my_result)
    return HttpResponse('It is Get request')


def render_name(request):
    if request.method == "GET":
        template = loader.get_template('form_name.html')
        return HttpResponse(template.render({}, request))
    if request.method == "POST":
        name = request.POST.get('name')
        template = loader.get_template('display_name.html')
        return HttpResponse(template.render({'name': name}, request))

# Create your views here.

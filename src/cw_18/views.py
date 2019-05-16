from django.shortcuts import render
from django.http import HttpResponse


def comment_count(request):
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
        result = f'Length comment is {len_com}, vowels is {count_vow}, consonant is {count_cons}'
        return HttpResponse(result)
    return HttpResponse('It is GET request')

def string_cut(request):
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


# Create your views here.

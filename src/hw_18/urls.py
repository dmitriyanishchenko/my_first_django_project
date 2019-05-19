from django.urls import path

from .views import line_to_file, file_to_list, return_form


urlpatterns = [

    path('line_to_file/', line_to_file),
    path('file_to_list/', file_to_list),
    path('return_form/', return_form),
]

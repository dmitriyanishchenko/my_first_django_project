from django.urls import path

from .views import line_to_file


urlpatterns = [

    path('line_to_file/', line_to_file),
]

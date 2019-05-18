from .views import comment_count, string_cut, render_name

from django.urls import path


urlpatterns = [

    path('cw_18_1/', comment_count),
    path('cw_18_2/', string_cut),
    path('render_name/', render_name),

]

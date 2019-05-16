from cw_18.views import comment_count
from cw_18.views import string_cut
from django.urls import path


urlpatterns = [

    path('cw_18_1/', comment_count),
    path('cw_18_2/', string_cut),
]

from django.urls import path
from cw_20.views import home


urlpatterns = [
    path('home/', home, name='home')
]
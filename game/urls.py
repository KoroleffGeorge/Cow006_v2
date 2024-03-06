"""App urls"""
from django.urls import path

from . import views


app_name = 'game'
urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
]

from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

]

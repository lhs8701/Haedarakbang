
from django.contrib import admin
from django.urls import path
from hdrb import views

app_name = 'hdrb'
urlpatterns = [
    path('', views.index, name='index')
]

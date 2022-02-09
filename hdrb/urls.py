from django.contrib import admin
from django.urls import path
from hdrb.views import base_views, reservation_views

app_name = 'hdrb'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('reservation/create/', reservation_views.reservation_create, name='reservation_create'),
]

from django.contrib import admin
from django.urls import path, include
from .views import layout

urlpatterns = [
    path('', layout, name='layout'),
]

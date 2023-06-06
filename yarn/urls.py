from django.contrib import admin
from django.urls import path, include
from .views import yarns

urlpatterns = [
    path('', yarns, name='yarns'),
]

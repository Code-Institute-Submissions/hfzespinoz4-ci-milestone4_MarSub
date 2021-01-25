from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # This is the root URL
    path('', views.index, name='home')
]

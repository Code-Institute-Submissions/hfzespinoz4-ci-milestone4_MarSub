from django.urls import path
from . import views

urlpatterns = [
    # This is the root URL
    path('', views.all_services, name='services')
]

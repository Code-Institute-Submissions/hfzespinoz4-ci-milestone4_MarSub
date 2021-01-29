from django.urls import path
from . import views

urlpatterns = [
    # This is the root URL
    path('', views.view_bag, name='view_bag')
]

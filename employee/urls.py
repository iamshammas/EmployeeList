from django.contrib import admin
from django.urls import path

from .models import Employee
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pk>',views.emp_details,name='emp_details'),
]

from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
    data = Employee.objects.all()
    context = {
        'data': data
    }
    return render(request,'home.html',context)
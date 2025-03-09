from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Employee

def index(request):
    return HttpResponse('<h1>NICE TRY</h1>')

def emp_details(request,pk):
    details = get_object_or_404(Employee,pk=pk)
    context = {
        'details': details
    }
    return render(request,'emp_detail.html',context)
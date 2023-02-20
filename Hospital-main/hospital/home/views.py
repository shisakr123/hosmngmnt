from django.shortcuts import render
from .models import Departments,Doctors

from .forms import BookingForm

def departments(request):
    dict_dpt={
        'dpt':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dpt)

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def base(request):
    return render(request,'base.html')  

def booking(request):
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form) 
    
    

def contacts(request):
    return render(request,'contacts.html')   

# def departments(request):
#     return render(request,'departments.html')   

def doctors(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)          


# Create your views here.

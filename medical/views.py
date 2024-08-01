from django.http import HttpResponse
from django.shortcuts import render
from .models import Doctors
# Create your views here.

def medical(request):
    doc = Doctors.objects.all()
    return render(request,'medical.html',{'doc':doc})


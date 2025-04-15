from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'mjengocheck/home.html',{'title':'Home'})

def about(request):
    return render(request,'mjengocheck/about.html',{'title':'About'})
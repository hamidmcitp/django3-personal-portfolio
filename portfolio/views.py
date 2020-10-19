from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectHamidBagheri

def home (request):
    projects = ProjectHamidBagheri.objects.all()
    return render(request,'portfolio/home.html', {'projects':projects})

def about(request):
    return render(request , 'portfolio/about.html')



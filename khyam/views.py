from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request,'home.html')
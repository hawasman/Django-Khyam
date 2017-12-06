from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import users
# Create your views here.

def index(request,user_id):
    user_data = get_object_or_404(users,id=user_id)
    template = loader.get_template('Accuounts/user.html')
    context = {'user':user_data}
    return HttpResponse(template.render(context,request))

def reg(request):
    template = loader.get_template('Accuounts/register.html')
    return HttpResponse(render(request,'Accuounts/register.html'))
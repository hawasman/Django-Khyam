from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import users
from .forms import RegisterForm
# Create your views here.

def index(request,user_id=0,user_name=''):
    if user_id != 0:
        user_data = get_object_or_404(users,id=user_id)
    if user_name != '':
        user_data = get_object_or_404(users,username=user_name)
    template = loader.get_template('Accuounts/user.html')
    context = {'user':user_data}
    return HttpResponse(template.render(context,request))

def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('user',user_name=form.username)
    else:
        form = RegisterForm()
    return render(request,'Accuounts/register.html', {'form': form})

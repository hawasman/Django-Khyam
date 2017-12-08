from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import users
from .forms import RegisterForm,LoginForm
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
            user = form.save(commit=False)
            user.save()
            return redirect('user',user_name=user.id)
    else:
        form = RegisterForm()
    return render(request,'Accuounts/register.html', {'form': form})

def login(request,user_name = '',pass_word = ''):
    if request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            #TODO check login and password and do session integration
            return redirect('home')
    else:
        form = LoginForm()
    return render(request,'Accuounts/login.html', {'form': form})

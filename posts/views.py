from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from posts import models
from .forms import PostForm
from django.utils import timezone
# Create your views here.
def index(request):
	posts = models.post.objects.order_by('-pub_date')[:5]
	template = loader.get_template('posts/posts.html')
	context = {'posts': posts,}
	return HttpResponse(template.render(context, request))

def post(request,post_id):
	post_data = models.post.objects.get(id=post_id)
	template = loader.get_template('posts/post.html')
	context = {'post': post_data,}
	return HttpResponse(template.render(context, request))

def new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			newpost = form.save(commit=False)
			newpost.pub_date = timezone.now()
			newpost.rate = 0
			newpost.save()
			return redirect('post',newpost.id)
	else:
		template = loader.get_template('posts/new.html')
		form = PostForm()
	return render(request,'posts/new.html',{'form':form,})

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from posts import models

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

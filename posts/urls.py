from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='newpost'),
    path('<int:post_id>/', views.post, name='post'),
]
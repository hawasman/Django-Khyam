from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.reg, name='register'),
    path('login/', views.login, name='login'),
    path('<int:user_id>/', views.index, name='user'),
    path('<str:user_name>/', views.index, name='user'),
    
]

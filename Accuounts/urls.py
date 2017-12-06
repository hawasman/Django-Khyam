from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.index, name='user'),
    path('register/', views.reg, name='register'),
]
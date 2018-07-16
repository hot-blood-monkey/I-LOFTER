from django.urls import path
from . import views


urlpatterns =[
    path(r'', views.user_login, name='login'),
    path(r'login/', views.user_login, name='login'),
    path(r'register/', views.register, name='register'),
    path(r'register_done/', views.register, name='register_done'),
]
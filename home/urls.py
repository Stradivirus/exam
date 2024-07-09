from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('index', redirect_to_login, name='index'),
    path('', views.login_view, name='login'),
]
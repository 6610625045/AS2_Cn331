# login-logout/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from . import views



urlpatterns = [ 
    path('', auth_views.LoginView.as_view(template_name='login-logout/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),  # เส้นทางไปยังหน้าหลัก
]

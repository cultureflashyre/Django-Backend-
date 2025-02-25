from django.urls import path
from . import views

urlpatterns = [
    path('signup-corporate/', views.signup_corporate, name='signup_corporate'),
    path('login-corporate/', views.login_corporate, name='login_corporate'),
]
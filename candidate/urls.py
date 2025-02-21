from django.urls import path
from . import views

urlpatterns = [
    path('signup-candidate/', views.signup_candidate, name='signup_candidate'),
    path('login-candidate/', views.login_candidate, name='login_candidate'),
]
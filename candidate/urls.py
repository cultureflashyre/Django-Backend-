from django.urls import path
from . import views

urlpatterns = [
    path('signup-candidate/', views.signup_candidate, name='signup_candidate'),
    path('login-candidate/', views.login_candidate, name='login_candidate'),
    path('check-phone/', views.check_phone, name='check_phone'),
    path('check-email/', views.check_email, name='check_email'),
]
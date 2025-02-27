# accounts/urls.py

from django.urls import path
from .views import SignupView, LoginView
from . import views

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),  # New login endpoint
    path('check-phone/', views.check_phone, name='check_phone'),
    path('check-email/', views.check_email, name='check_email'),
]
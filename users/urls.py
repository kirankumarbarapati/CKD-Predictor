# FILE:  users/urls.py
# This is the URL file for ONLY the 'users' app.

from django.urls import path
from . import views  # Import views from the same app

# This list must be named 'urlpatterns'
urlpatterns = [
    # This creates the URL for your registration page at /register/
    path('register/', views.register, name='register'),
]
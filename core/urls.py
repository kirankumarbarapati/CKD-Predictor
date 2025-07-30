# FILE:  core/urls.py
# This is the main URL file for the whole project.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Route for the admin site
    path('admin/', admin.site.urls),

    # This includes Django's built-in auth URLs (for login, logout, etc.)
    # It makes them available at the top level, e.g., /login/
    path('', include('django.contrib.auth.urls')),

    # This includes the URLs from your 'users' app (like /register/)
    path('', include('users.urls')),

    # This includes the URLs from your 'prediction' app (your homepage)
    path('', include('prediction.urls')),
]
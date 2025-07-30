# prediction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This creates a URL for the root path '' that calls the 'predict_page' function from views.py
    path('', views.predict_page, name='predict_page'),
]
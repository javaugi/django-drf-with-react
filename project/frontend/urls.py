"""
In this file we’ll wire up the view to our root:
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
]
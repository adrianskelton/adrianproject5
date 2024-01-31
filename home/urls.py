from django.contrib import admin
from django.contrib.sites.models import Site
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

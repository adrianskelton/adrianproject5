from django.contrib.sites.models import Site
from django.urls import path, include
from . import views
from .views import contact

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_form'),
]



from django.contrib.sites.models import Site
from django.urls import path, include
from . import views
from .views import artist_detail

urlpatterns = [
    path('artist_detail/<int:pk>/', artist_detail, name='artist_detail'),
]

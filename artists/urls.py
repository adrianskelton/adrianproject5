from django.contrib.sites.models import Site
from django.urls import path, include
from . import views
from .views import artist_detail, artist_list

urlpatterns = [
    path('artist_detail/<int:pk>/', artist_detail, name='artist_detail'),
    path('artist_list/', artist_list, name='artist_list'),
]

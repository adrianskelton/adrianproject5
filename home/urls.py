from django.contrib.sites.models import Site
from django.urls import path, include
from . import views
from .views import contact


handler404 = 'home.views.custom_404'
handler400 = 'home.views.custom_400'
handler500 = 'home.views.custom_500'

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_form'),
]



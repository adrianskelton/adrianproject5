from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_form'),
    path('404', views.custom_404, name='404'),
    path('500', views.custom_500, name='500'),
]



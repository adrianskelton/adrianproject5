from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog_view, name='blog_view'),  
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.new_post, name='create_post'),
]

from django.urls import path
from . import views
from .views import edit_comment, delete_comment

urlpatterns = [
    path('', views.blog_view, name='blog_view'),  
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.new_post, name='create_post'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
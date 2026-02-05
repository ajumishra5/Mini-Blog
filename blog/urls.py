from django.urls import path
from .views import post_list, create_post, post_detail, edit_post, delete_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
]
from django.urls import path
from .views import post_list, create_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', create_post, name='create_post'),
]
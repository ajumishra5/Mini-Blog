from django.urls import path
from .views import (
    post_list,
    post_detail,
    create_post,
    edit_post,
    delete_post,
    profile_view,
    toggle_like,
    signup_view,
    profile_view,
)

urlpatterns = [
    path("", post_list, name="post_list"),
    path("create/", create_post, name="create_post"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", edit_post, name="edit_post"),
    path("post/<int:pk>/delete/", delete_post, name="delete_post"),
    path("post/<int:pk>/like/", toggle_like, name="toggle_like"),
    path("signup/", signup_view, name="signup"),
    path("profile/<str:username>/", profile_view, name="profile"),
]

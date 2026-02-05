from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, SignUpForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib import messages
from .models import Like, Post


# View to list all posts with pagination
def post_list(request):
    post_list = Post.objects.all().order_by("-created_at")
    paginator = Paginator(post_list, 5)  # 5 posts per page

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    return render(request, "blog/post_list.html", {"posts": posts})


# View to create a new post
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # auto author set
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("post_list")
    else:
        form = PostForm()  # empty form for GET request

    return render(
        request, "blog/create_post.html", {"form": form}
    )  # View to see post details and comments


# View to see post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


# View to edit an existing post
@login_required  # Ensure user is logged in
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Only allow the author to edit the post
    if request.user != post.author:
        return redirect("post_list")

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, "Post updated successfully!")
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)  # Pre-fill form with existing post data

    return render(request, "blog/edit_post.html", {"form": form})


# View to delete a post
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Only allow the author to delete the post
    if request.user != post.author:
        return redirect("post_detail", pk=post.pk)

    if request.method == "POST":
        post.delete()
        messages.warning(request, "Post deleted!")
        return redirect("post_list")

    return render(request, "blog/delete_post.html", {"post": post})


# View to see post details and handle comments
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by(
        "-created_at"
    )  # Handle new comment submission

    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )


# Ajax view to toggle like/unlike a post
@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({"liked": liked, "likes_count": post.likes.count()})


# User signup view
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            return redirect("post_list")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


# User profile view
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    post_list = user.posts.all().order_by("-created_at")

    paginator = Paginator(post_list, 5)  # 5 posts per page
    page_number = request.GET.get("page")  # Get current page number
    posts = paginator.get_page(page_number)  # Get posts for the current page

    return render(request, "blog/profile.html", {"profile_user": user, "posts": posts})

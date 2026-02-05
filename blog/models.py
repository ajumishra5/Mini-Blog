from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )  # Each post is linked to a user (author)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )  # Each comment is linked to a post
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Each comment is linked to a user (author)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes"
    )  # Each like is linked to a post
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Each like is linked to a user

    class Meta:
        unique_together = ("post", "user")  # Ensure a user can like a post only once

    def __str__(self):
        return f"{self.user} liked {self.post}"

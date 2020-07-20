from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title + "Post"


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return f"Like from {self.author} to {self.post}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    message = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.message}"

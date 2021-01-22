from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(upload_to="posts")
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, default=now, editable=True)

    def __str__(self):
        return f"Post by {self.author}"

    class Meta:
        ordering = ["-created_date"]


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

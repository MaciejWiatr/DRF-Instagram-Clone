from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    age = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(
        default="default_prof_pic.jpg", upload_to="profile_pics")
    follows = models.ManyToManyField("UserProfile", related_name="followed_by")
    description = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return f"{self.user.username} profile"

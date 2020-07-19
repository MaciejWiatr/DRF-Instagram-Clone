from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print('siemanaoooo')
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

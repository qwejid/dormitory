from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from account.models import Profile
from django.contrib.auth.models import User
import os


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



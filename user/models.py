import os
import shutil

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=32, blank=True, null=True)

    @property
    def home_dir_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    user_profile = UserProfile(user=instance, display_name=instance.username)
    user_profile.save()


@receiver(post_save, sender=UserProfile)
def create_user_folder(sender, instance, created, **kwargs):
    if not created:
        return

    user_dir = instance.home_dir_path
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)


@receiver(pre_delete, sender=UserProfile)
def delete_user_folder(sender, instance, **kwargs):
    user_dir = instance.home_dir_path
    if os.path.exists(user_dir):
        shutil.rmtree(user_dir)

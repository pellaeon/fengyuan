import os

from django.contrib.auth.models import User
from django.db import models
from django.settings import MEDIA_ROOT


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    display_name = models.CharField(max_length=32, blank=True, null=True)

    @property
    def home_dir(self):
        return os.path.join(MEDIA_ROOT, user.username)

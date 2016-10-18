import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=32, blank=True, null=True)

    @property
    def home_dir_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.user.username)

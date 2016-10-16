import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    display_name = models.CharField(max_length=32, blank=True, null=True)

    def get_home_dir(self):
        return os.path.join(settings.MEDIA_ROOT, user.username)

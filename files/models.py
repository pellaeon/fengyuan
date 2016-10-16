import os
import uuid

from django.db import models
from django.utils import timezone
from polymorphic_tree.models import (PolymorphicMPTTModel,
                                     PolymorphicTreeForeignKey)


class FYNode(PolymorphicMPTTModel):
    """
    Base data hierarchy node

    FYNode should be used as base class for all data hierarchy object models.
    """
    parent = PolymorphicTreeForeignKey('self', blank=True, null=True,
                                       related_name='children')
    name = models.CharField(max_length=200)
    gid = models.UUIDField(default=uuid.uuid4, editable=False)  # global id


class Inode(FYNode):
    """
    Actual file/dir existing in filesystem
    """
    owner = models.ForeignKey(User)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    size = models.BigIntegerField(
        null=True, blank=True)  # null means unknown size


class Directory(Inode):
    path = models.FilePathField(
        path=owner.profile.home_dir, recursive=True, allow_folders=True, allow_files=False)

    @property
    def name(self):
        return os.path.basename(self.path)

# TODO class RootDirectory(Directory)
# Future: different FileStorage class configured in RootDirectory
# TODO class File(Inode)

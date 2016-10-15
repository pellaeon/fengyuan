import uuid
from django.db import models
from polymorphic_tree.models import (PolymorphicMPTTModel, 
    PolymorphicTreeForeignKey
)

class FYNode(PolymorphicMPTTModel):
    """
    Base data hierarchy node

    FYNode should be used as base class for all data hierarchy object models.
    """
    parent = PolymorphicTreeForeignKey('self', blank=True, null=True,
            related_name='children')
    name = models.CharField(max_length=200)
    gid = models.UUIDField(default=uuid.uuid4, editable=False) # global id

# TODO class Inode(FYNode), actual file/dir existing in filesystem
# TODO class Directory(Inode)
# TODO class RootDirectory(Directory)
# Future: different FileStorage class configured in RootDirectory
# TODO class File(Inode)

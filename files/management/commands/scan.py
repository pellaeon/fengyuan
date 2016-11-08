import os

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError

from files.models import Directory, File


# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
class Command(BaseCommand):
    help = (
        'Recursively scans the directories and files '
        'of the "files/" dir for a specific username, '
        'and save those direcoties and files into database.'
    )
    USER_FILES_DIR_NAME = 'files'

    def add_arguments(self, parser):
        parser.add_argument(
            'username',
            type=str,
            help='The username which exists in the User model.',
        )

    def handle(self, *args, **options):
        username = options['username']

        try:
            user = User.objects.get(username=username)
        except:
            raise CommandError(
                (
                    "username: {} doesn't exists in the User model."
                ).format(username)
            )

        user_dir = user.profile.home_dir_path
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        user_files_dir = os.path.join(user_dir, self.USER_FILES_DIR_NAME)
        if not os.path.exists(user_files_dir):
            os.makedirs(user_files_dir)

        parent_dir = None
        for current_dir_path, subdirs, files in os.walk(user_files_dir):
            try:
                current_dir = Directory.objects.get(
                    name=os.path.basename(current_dir_path),
                    owner=user,
                    path=current_dir_path,
                )
            except ObjectDoesNotExist:
                current_dir = Directory(
                    parent=parent_dir,
                    name=os.path.basename(current_dir_path),
                    owner=user,
                    path=current_dir_path,
                )
                current_dir.save()
            except:
                raise

            for _file in files:
                try:
                    f = File.objects.get(
                        parent=current_dir,
                        name=_file,
                        owner=user,
                    )
                except ObjectDoesNotExist:
                    f = File(
                        parent=current_dir,
                        name=_file,
                        owner=user,
                        size=os.path.getsize(
                            os.path.join(current_dir_path, _file)
                        ),
                    )
                    f.save()
                except:
                    raise

            parent_dir = current_dir

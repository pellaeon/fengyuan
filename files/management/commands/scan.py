import os

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError

from files.models import Directory, File


# https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'Recursively scans the directories and files of the "files/" dir for a specific username, and save those direcoties and files into database. '
    USER_FILES_DIR_NAME = 'files'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str,
                            help='The username which exists in the User model.')

    def handle(self, *args, **options):
        username = options['username']

        try:
            user = User.objects.get(username=username)
        except:
            raise CommandError(
                "username: {} doesn't exists in the User model.".format(username))

        user_dir = user.profile.home_dir_path
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        user_files_dir = os.path.join(user_dir, self.USER_FILES_DIR_NAME)
        if not os.path.exists(user_files_dir):
            os.makedirs(user_files_dir)

        for current_dir, subdirs, files in os.walk(user_files_dir):
            try:
                parent_dir = Directory.objects.get(name=os.path.basename(
                    current_dir), owner=user, path=current_dir)
            except ObjectDoesNotExist:
                parent_dir = Directory(name=os.path.basename(
                    current_dir), owner=user, path=current_dir)
                parent_dir.save()
            except:
                raise

            for file in files:
                try:
                    f = File.objects.get(
                        parent=parent_dir, name=file, owner=user)
                except ObjectDoesNotExist:
                    f = File(parent=parent_dir, name=file, owner=user,
                             size=os.path.getsize(os.path.join(current_dir, file)))
                    f.save()
                except:
                    raise

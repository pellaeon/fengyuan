import os

from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import models
from django.test import TestCase

from files.models import Directory, File


class ManagementCommandsScanTest(TestCase):
    def setUp(self):
        '''
        user_home_dir/
            dx/
            fx
            files/
                a
                b/
                    c
                    d/
        '''

        self.user = User.objects.create_user(
            username='fake-user-for-testing',
            email='test@test.com',
            password='test')
        user_home_dir = self.user.profile.home_dir_path

        dir_should_not_be_scanned = os.path.join(user_home_dir, 'dx')
        os.mkdir(dir_should_not_be_scanned)

        file_should_not_be_scanned = os.path.join(user_home_dir, 'fx')
        os.mknod(file_should_not_be_scanned)

        user_files_dir = os.path.join(self.user.profile.home_dir_path, 'files')
        os.mkdir(user_files_dir)

        file_a = os.path.join(user_files_dir, 'a')
        os.mknod(file_a)

        dir_b = os.path.join(user_files_dir, 'b')
        os.mkdir(dir_b)

        file_c_in_dir_b = os.path.join(dir_b, 'c')
        os.mknod(file_c_in_dir_b)

        dir_d_in_dir_b = os.path.join(dir_b, 'd')
        os.mkdir(dir_d_in_dir_b)

        call_command('scan', self.user.username)

    def test_file_should_not_be_scanned(self):
        with self.assertRaises(models.ObjectDoesNotExist):
            File.objects.get(name='fx')

    def test_dir_should_not_be_scanned(self):
        with self.assertRaises(models.ObjectDoesNotExist):
            Directory.objects.get(name='dx')

    def test_files_should_be_scanned(self):
        for file_name in ('a', 'c'):
            self.assertIsInstance(File.objects.get(name=file_name), File)

    def test_dirs_should_be_scanned(self):
        for dir_name in ('files', 'b', 'd'):
            self.assertIsInstance(
                Directory.objects.get(name=dir_name), Directory)

    def test_owner_of_files(self):
        for file_name in ('a', 'c'):
            node = File.objects.get(name=file_name)
            self.assertEqual(self.user.id, node.owner_id)

    def test_owner_of_dirs(self):
        for dir_name in ('files', 'b', 'd'):
            node = Directory.objects.get(name=dir_name)
            self.assertEqual(self.user.id, node.owner_id)

    def test_created_time(self):
        for f in File.objects.all():
            self.assertTrue(f.created)

        for d in Directory.objects.all():
            self.assertTrue(d.created)

    def test_updated_time(self):
        for f in File.objects.all():
            self.assertTrue(f.updated)

        for d in Directory.objects.all():
            self.assertTrue(d.updated)

    def test_parent(self):
        # The parent of file c and dir d is dir b
        self.assertEqual(
            Directory.objects.get(name='b').id,
            File.objects.get(name='c').parent.id, )
        self.assertEqual(
            Directory.objects.get(name='b').id,
            Directory.objects.get(name='d').parent.id, )

        # The parent of file a and dir b is dir files
        self.assertEqual(
            Directory.objects.get(name='files').id,
            File.objects.get(name='a').parent.id, )
        self.assertEqual(
            Directory.objects.get(name='files').id,
            Directory.objects.get(name='b').parent.id, )

    def tearDown(self):
        self.user.delete()

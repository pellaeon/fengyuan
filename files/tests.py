import os

from django.contrib.auth.models import User
from django.core.management import call_command
from django.db import models
from django.test import TestCase

from files.models import FYNode


class ManagementCommandsScanTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='fake-user-for-testing', email='test@test.com', password='test')
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

    def test_file_and_dir_should_not_be_scanned(self):
        with self.assertRaises(models.ObjectDoesNotExist):
            FYNode.objects.get(name='fx')

        with self.assertRaises(models.ObjectDoesNotExist):
            FYNode.objects.get(name='dx')

    def test_file_and_dir_should_be_scanned(self):
        self.assertIsInstance(FYNode.objects.get(name='files'), FYNode)
        self.assertIsInstance(FYNode.objects.get(name='a'), FYNode)
        self.assertIsInstance(FYNode.objects.get(name='b'), FYNode)
        self.assertIsInstance(FYNode.objects.get(name='c'), FYNode)
        self.assertIsInstance(FYNode.objects.get(name='d'), FYNode)

    def tearDown(self):
        self.user.delete()

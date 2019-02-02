from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError

from tasklist.models import Task


class TaskModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='joe',
            email='jstrummer@theclash.com',
            password='brixton'
        )

    def test_create_valid_task(self):
        task = Task.objects.create(
            user=self.user, title="title", description="desc"
        )
        self.assertIsInstance(task, Task)
        self.assertIn(task, Task.objects.all())

    def test_create_task_missing_user(self):
        with self.assertRaises(IntegrityError):
            task = Task.objects.create(
                title='title', description="desc"
            )

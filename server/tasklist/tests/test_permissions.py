from uuid import uuid4

from mock import MagicMock

from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError

from tasklist.models import Task
from tasklist.permissions import IsOwnerOrReadOnly

class IsOwnerOrReadOnlyPermissionsTestCase(TestCase):

    def setUp(self):
        self.user_1 = self._create_user({
            'username': 'user1',
            'password': 'user1'
        })
        self.user_2 = self._create_user({
            'username': 'user2',
            'password': 'user2'
        })

        self.permission = IsOwnerOrReadOnly()
        self.view = MagicMock()
        self.user1_task = self._create_task(user=self.user_1)
        self.user2_task = self._create_task(user=self.user_2)

    def test_get_object(self):
        request = MagicMock(user=self.user_1, method='GET')
        permission = self.permission.has_object_permission(
            request=request,
            view=self.view,
            obj=self.user1_task 
        )
        self.assertTrue(permission)
    
    def test_patch_task_with_owner(self):
        request = MagicMock(user=self.user_1, method='PATCH')
        permission = self.permission.has_object_permission(
            request=request,
            view=self.view,
            obj=self.user1_task 
        )
        self.assertTrue(permission)


    def test_put_task_with_owner(self):
        request = MagicMock(user=self.user_1, method='PUT')
        permission = self.permission.has_object_permission(
            request=request,
            view=self.view,
            obj=self.user1_task 
        )
        self.assertTrue(permission)


    def test_patch_task_with_non_owner(self):
        request = MagicMock(user=self.user_2, method='PATCH')
        permission = self.permission.has_object_permission(
            request=request,
            view=self.view,
            obj=self.user1_task 
        )
        self.assertTrue(permission)
    
    def test_put_task_with_non_owner(self):
        request = MagicMock(user=self.user_2, method='PUT')
        permission = self.permission.has_object_permission(
            request=request,
            view=self.view,
            obj=self.user1_task 
        )
        self.assertFalse(permission)

    def _create_user(self, credentials):
        return User.objects.create_user(**credentials)

    def _create_task(self, user):
        return Task.objects.create(user=user, title=str(uuid4()), description='Description')

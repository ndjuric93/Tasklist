from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.test import APIClient

from tasklist.models import Task


class TaskViewTestCase(TestCase):

    def setUp(self):
        """
        Set up of test case by creating and logging in a user.
        DRF APIClient is added due to limitations of Django TestClient
        """
        self.credentials = {
            'username': 'joestrummer',
            'password': 'brixton'
        }
        self.user = User.objects.create_user(**self.credentials)
        
        self.client = APIClient()
        self.client.login(**self.credentials)


    def test_get_tasks(self):
        """ Test standard fetch of tasks """
        tasks = [
            {
                'title': 'title1',
                'description': 'description1'
            },
            {
                'title': 'title2',
                'description': 'description2'
            }
        ]
        Task.objects.create(user=self.user, **tasks[0])
        Task.objects.create(user=self.user, **tasks[1])
        response = self.client.get(
            path=reverse('task-list')
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), len(tasks))
        for i in range(0, len(response.data)):
            self.assertDictEqual(
                tasks[i], 
                {
                    'title': response.data[i]['title'],
                    'description': response.data[i]['description']
                }
            )

    def test_create_task(self):
        """ Test standard task creation """
        data = {
            'title': 'Title',
            'description': 'Description'
        }

        response = self.client.post(
            path=reverse('task-list'),
            data=data
        )
        task = Task.objects.get(pk=response.data['id'])
        self.assertIsNotNone(task)
        self.assertEqual(data['title'], task.title)
        self.assertEqual(data['description'], task.description)
        self.assertTrue(status.is_success(response.status_code))

    def test_create_task_without_title(self):
        """ Test standard task creation with ommited title """
        data = {
            'description': 'Description'
        }
        response = self.client.post(
            path=reverse('task-list'),
            data=data
        )
        self.assertTrue(status.is_client_error(response.status_code))

    def test_create_task_without_description(self):
        """ Test standard task creation with ommited description """
        data = {
            'title': 'Title'
        }
        response = self.client.post(
            path=reverse('task-list'),
            data=data
        )
        self.assertTrue(status.is_client_error(response.status_code))


    def test_create_task_without_title_and_description(self):
        """ Test standard task creation with ommited data """
        response = self.client.post(
            path=reverse('task-list'),
            data={}
        )
        self.assertTrue(status.is_client_error(response.status_code))


    def test_edit_task(self):
        """ Test standard task editing """
        task = Task.objects.create(user=self.user, title='TitleToEdit', description='DescriptionToEdit')
        new_data = {
            'title': 'EditedTitle',
            'description': 'EditedDescription'
        }
        response = self.client.put(
            path='/task/' + str(task.id) + '/',
            data=new_data
        )

        updated_task = Task.objects.get(pk=task.id)
        task_data = {
            'title': updated_task.title,
            'description': updated_task.description
        }
        self.assertTrue(status.is_success(response.status_code))
        self.assertDictEqual(task_data, new_data)

    def test_edit_other_user_task(self):
        new_user = User.objects.create_user(username="temp_test_user", password="temp")
        task = Task.objects.create(user=new_user, title='TitleToEdit', description='DescriptionToEdit')

        response = self.client.put(
            path='/task/' + str(task.id) + '/',
            data={
                'title': 'EditedTitle',
                'description': 'EditedDescription'
            }
        )
        self.assertTrue(status.is_client_error(response.status_code))

    
    def test_task_done(self):
        """ Test done standard tas """
        task = Task.objects.create(user=self.user, title='DoneTitle', description='DoneDescription')
        response = self.client.patch(
            path='/task/' + str(task.id) + '/',
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Task.objects.get(pk=task.id).done_by, self.user)

    
    def test_task_delete(self):
        """ Test done standard tas """
        task = Task.objects.create(user=self.user, title='TaskToBeDeleted', description='DescriptionToBeDeleted')
        response = self.client.delete(
            path='/task/' + str(task.id) + '/',
        )
        self.assertTrue(status.is_success(response.status_code))
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(pk=task.id)

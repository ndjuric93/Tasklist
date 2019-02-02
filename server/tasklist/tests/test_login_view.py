from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='joe',
            email='jstrummer@theclash.com',
            password='brixton'
        )

    def test_successful_login(self):
        response = self.client.post(
            path='/login/',
            data={
                'username':'joe',
                'password':'brixton'
            }
        )
        self.assertTrue(status.is_success(response.status_code))

    def test_failed_login(self):
        response = self.client.post(
            path='/login/',
            data={
                'username':'unexisting_user',
                'password':'wrong_password'
            }
        )
        self.assertTrue(status.is_client_error(response.status_code))

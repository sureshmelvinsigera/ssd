from audioop import reverse

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import APIClient
from .models import Astronaut, User


class APITestCase(APITestCase):
    """
    API test case for user login
    """
    data = {}

    @classmethod
    def setUpClass(self):
        """
        set up initial data for astronaut object
        """
        self.data = {"username": "markV", "password": "u73dg2626_#4"}
        user = Astronaut.objects.create(username=self.data['username'])
        user.set_password(self.data['password'])
        user.save()

    @classmethod
    def tearDownClass(cls):
        """
        required by Django or else it will trigger
        AttributeError: type object 'APITestCase' has no attribute 'cls_atomics'
        """
        pass

    def test_login(self):
        """
        user login test
        """
        # create new API instance
        temp_client = APIClient()
        # pass user information the login end point
        response = temp_client.post("http://127.0.0.1:8000/auth/users/astronaut/login/", data=self.data, follow=True)
        # print(response.data)
        # token = response.data["token"]
        # expected result from the end point
        expected = {
            "username": "username",
            "email": "email",
            "token": "token"
        }
        # check if expected matched with actual result
        self.assertTrue(expected.keys() >= response.data.keys())

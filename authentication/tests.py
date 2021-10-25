from audioop import reverse

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import APIClient
from .models import Astronaut, Scientist, User


class APITestCase(APITestCase):
    """
    API test case for user login
    """
    data = {}
    scientist = {}

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
        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/astronaut/login/", data=self.data, follow=True)
        # expected result from the end point
        expected = {
            "username": "username",
            "email": "email",
            "token": "token"
        }
        # check if expected matched with actual result
        self.assertTrue(expected.keys() >= response.data.keys())

    def test_astronaut_registration_fails_when_password_too_short(self):
        temp_client = APIClient()
        registration_details = {
            "username": "test_user",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password": "1234"
        }

        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/astronaut/register/", data=registration_details, follow=True)

        self.assertEqual(
            response.data["password"][0], "Ensure this field has at least 8 characters.")
        self.assertEqual(response.status_code, 400)

    def test_scientist_registration_fails_when_password_too_short(self):
        temp_client = APIClient()
        registration_details = {
            "username": "test_user",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password": "1234"
        }

        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/scientist/register/", data=registration_details, follow=True)

        self.assertEqual(
            response.data["password"][0], "Ensure this field has at least 8 characters.")
        self.assertEqual(response.status_code, 400)

    def test_scientist_registration_successful_if_password_valid(self):
        temp_client = APIClient()
        registration_details = {
            "username": "test_user",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password": "Y+w=6[MQWNt$quy"
        }

        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/scientist/register/", data=registration_details, follow=True)

        self.assertEqual(response.status_code, 201)

    def test_astronaut_registration_successful_if_password_valid(self):
        temp_client = APIClient()
        registration_details = {
            "username": "test_user",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@test.com",
            "password": "Y+w=6[MQWNt$quy"
        }

        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/astronaut/register/", data=registration_details, follow=True)

        self.assertEqual(response.status_code, 201)

    def test_health_report_upload(self):
        temp_client = APIClient()
        # Log in with dummy credentials
        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/astronaut/login/", data=self.data, follow=True)

        # Get token and apply it to headers
        token = response.data["token"]
        temp_client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        # Add a record
        record = {
            "weight": 155,
            "blood_type": "B",
            "blood_pressure": 120,
            "heart_rate": 80,
            "muscle_mass": 34
        }

        response = temp_client.post(
            "http://127.0.0.1:8000/astronaut/health-reports/", data=record, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_health_report_retrieval(self):
        temp_client = APIClient()
        # Log in with dummy credentials
        response = temp_client.post(
            "http://127.0.0.1:8000/auth/users/astronaut/login/", data=self.data, follow=True)

        # Get token and apply it to headers
        token = response.data["token"]
        temp_client.credentials(HTTP_AUTHORIZATION="JWT " + token)

        # Add a record
        record = {
            "weight": 155,
            "blood_type": "B",
            "blood_pressure": 120,
            "heart_rate": 80,
            "muscle_mass": 34
        }

        temp_client.post(
            "http://127.0.0.1:8000/astronaut/health-reports/", data=record, follow=True)

        # Read the record back from the API and verify
        health_record = temp_client.get(
            "http://127.0.0.1:8000/astronaut/health-reports/1", data=None, follow=True)

        self.assertEqual(health_record.status_code, 200)
        self.assertEqual(health_record.data["id"], 1)
        self.assertEqual(health_record.data["weight"], 155)
        self.assertEqual(health_record.data["blood_type"], "B")
        self.assertEqual(health_record.data["blood_pressure"], 120)
        self.assertEqual(health_record.data["heart_rate"], 80)
        self.assertEqual(
            health_record.data["feedback"], "No feedback as of yet")

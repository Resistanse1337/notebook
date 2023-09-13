from django.urls import reverse
from django.test import Client
from rest_framework.test import APITestCase

from users.models import User


class APITestBase(APITestCase):
    def setUp(self) -> None:
        csrf_url = reverse("csrf")
        csrf_token = self.client.get(csrf_url).json()["csrfToken"]

        self.csrf_client = Client(headers={"X-CSRFToken": csrf_token})

        self.register_data = {
            "first_name": "Alex",
            "last_name": "Ivanov",
            "username": "Ivalex",
            "email": "user@example.com",
        }
        self.credentials = {
            "username": "Ivalex",
            "password": "pass12345",
            "password_confirm": "pass12345",
        }
    
    def _register_and_login(self):
        register_data= self.register_data
        register_data.update(self.credentials)

        User.create_user(register_data)

        login_url = reverse("login")

        login_response = self.csrf_client.post(login_url, data=self.credentials)

        return login_response
    
    def _print_result(self, test_name, result):
        print(f"\n{test_name} result: {result}\n")
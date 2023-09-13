from django.urls import reverse

from common.test import APITestBase


class RegisterAuthTestCase(APITestBase):
    def test_register(self):
        register_url = reverse("register")

        register_data = self.register_data
        register_data.update(self.credentials)

        response = self.csrf_client.post(
            register_url,
            data=register_data,
        )
        self._print_result("register", response.json())
        
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self._register_and_login()
        self._print_result("login", response.content)

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self._register_and_login()

        logout_url = reverse("logout")

        response = self.csrf_client.post(logout_url)
        self._print_result("logout", response.content)

        self.assertEqual(response.status_code, 200)

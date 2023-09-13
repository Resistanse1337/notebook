from django.urls import reverse

from common.test import APITestBase
from contacts.models import Contact
from users.models import User


class ContactAPITestCase(APITestBase):
    def setUp(self) -> None:
        super().setUp()

        self._register_and_login()
        user = User.objects.first()

        self.contact_data = {
            "first_name": "First contact",
            "last_name": "lastname",
            "phone_number": 12345,
            "email": "test@mail.ru"
        }

        contact_1 = Contact.objects.create(
            user=user, 
            **self.contact_data
        )
        self.pk = contact_1.pk
        Contact.objects.create(
            user=user, 
            **self.contact_data
        )

    def test_list(self):
        url = reverse("contacts")

        response = self.csrf_client.get(url)
        self._print_result("contacts_list", response.json())

        self.assertEqual(response.status_code, 200)

    def test_create(self):
        url = reverse("contacts")

        response = self.csrf_client.post(url, data=self.contact_data)
        self._print_result("contact_create", response.json())

        self.assertEqual(response.status_code, 201)

    def test_get_one(self):
        url = reverse("contacts_single", kwargs={"pk": self.pk})
        
        response = self.csrf_client.get(url)
        self._print_result("get_single_contact", response.json())

        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        url = reverse("contacts_single", kwargs={"pk": self.pk})

        response = self.csrf_client.patch(url, data={"first_name": "NEW_NAME"}, content_type='application/json')
        self._print_result("patch_contact", response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.get(pk=self.pk).first_name, "NEW_NAME")

    def test_delete(self):
        url = reverse("contacts_single", kwargs={"pk": self.pk})

        response = self.csrf_client.delete(url)
        self._print_result("delete_contact", response.content)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Contact.objects.filter(pk=self.pk).first(), None)

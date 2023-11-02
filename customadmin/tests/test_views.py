from django.test import TestCase, Client
from django.urls import reverse

from customadmin.models import CustomUser, Item
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.edit_url = reverse("customadmin:edit-object", args=[1, "CustomUser"])
        self.user = CustomUser.objects.create(username="test", password="testpwd")

    def test_unlogin_edit_get(self):
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, 302)

    def test_login(self):
        self.client.login(username="test", password="testpwd")
        response = self.client.get(reverse("customadmin:login"))
        self.assertEquals(response.status_code, 200)

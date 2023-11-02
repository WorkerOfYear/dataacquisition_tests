from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from customadmin.views import dashboard


class TestUrls(SimpleTestCase):
    def test_dashboard_url_resolves(self):
        url = reverse("customadmin:dashboard")
        self.assertEqual(resolve(url).func, dashboard)

    def test_login_url_resolves(self):
        url = reverse("customadmin:login")
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

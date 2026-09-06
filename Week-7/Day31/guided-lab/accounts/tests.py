from django.test import TestCase
from django.urls import reverse


class AccountFlowTests(TestCase):

    def test_register_then_login_opens_profile(self):
        response = self.client.post(
            reverse("accounts:register"),
            {"username": "ali"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("accounts:login"))

        response = self.client.post(
            reverse("accounts:login"),
            {"username": "ali"},
            follow=True,
        )
        self.assertContains(response, "Welcome ali")

    def test_login_without_register_redirects_to_register(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:register"))

    def test_profile_requires_valid_login(self):
        response = self.client.get(reverse("accounts:profile"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:register"))

        self.client.post(reverse("accounts:register"), {"username": "sara"})
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "someone-else"},
            follow=True,
        )
        self.assertRedirects(response, reverse("accounts:register"))

from pathlib import Path

from django.contrib.auth import get_user_model
from django.contrib.flatpages.models import FlatPage
from django.contrib.staticfiles import finders
from django.test import TestCase


class AssignmentRequirementsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.regular_user = User.objects.create_user(
            username="student",
            password="student-pass-123",
            is_staff=False,
        )
        cls.admin_user = User.objects.create_user(
            username="admin",
            password="admin-pass-123",
            is_staff=True,
        )

    def test_exactly_three_flatpages_are_seeded(self):
        self.assertEqual(FlatPage.objects.count(), 3)
        self.assertSetEqual(
            set(FlatPage.objects.values_list("url", flat=True)),
            {"/about/", "/styled/", "/private/"},
        )

    def test_public_pages_are_available(self):
        self.assertEqual(self.client.get("/about/").status_code, 200)
        self.assertEqual(self.client.get("/styled/").status_code, 200)

    def test_styled_page_repeats_content_twice(self):
        page = FlatPage.objects.get(url="/styled/")
        response = self.client.get("/styled/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode().count(page.content), 2)

    def test_private_page_requires_staff_admin(self):
        anonymous_response = self.client.get("/private/")
        self.assertEqual(anonymous_response.status_code, 302)

        self.client.login(username="student", password="student-pass-123")
        regular_response = self.client.get("/private/")
        self.assertEqual(regular_response.status_code, 302)
        self.client.logout()

        self.client.login(username="admin", password="admin-pass-123")
        admin_response = self.client.get("/private/")
        self.assertEqual(admin_response.status_code, 200)

    def test_private_flatpage_is_marked_registration_required(self):
        self.assertTrue(FlatPage.objects.get(url="/private/").registration_required)

    def test_font_family_and_font_size_are_explicit(self):
        static_path = finders.find("css/site.css")
        self.assertIsNotNone(static_path)
        css = Path(static_path).read_text(encoding="utf-8")
        self.assertIn("font-family:", css)
        self.assertIn("font-size:", css)
        self.assertIn(".styled-page", css)

    def test_bootstrap_is_loaded_from_django_static(self):
        response = self.client.get("/about/")
        html = response.content.decode()
        self.assertIn("/static/vendor/bootstrap/css/bootstrap.min.css", html)
        self.assertIn("/static/vendor/bootstrap/js/bootstrap.bundle.min.js", html)

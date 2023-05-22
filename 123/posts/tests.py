from django.test import TestCase, Client
from django.urls import reverse


class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("posts/index.html")

    def test_about(self):
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed("posts/about.html")
        self.assertEqual(response.status_code, 200)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertTemplateUsed("posts/contacts.html")
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        response = self.client.get(reverse("post-update", 1))
        self.assertTemplateUsed("posts/iupdate_post.html")
        self.assertEqual(response.status_code, 200)

    def test_delete_post(self):
        response = self.client.get(reverse("post-delete", 1))
        self.assertTemplateUsed("posts/idelete_post.html")
        self.assertEqual(response.status_code, 200)
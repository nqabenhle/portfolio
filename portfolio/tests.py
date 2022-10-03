import json
from django.test import TestCase, Client
from django.db.utils import IntegrityError

from .models import *

# Create your tests here.
c = Client()

class PortfolioTestCase(TestCase):

    def setUp(self):
        # Create projects
        Project.objects.create(name="App", about="Great app", embed_link="ytlink", video_link="link", github_repo="repo")
        Project.objects.create(name="App", about="Great app", embed_link="ytlink", video_link="link", github_repo="repo")
        Project.objects.create(name="App", about="Great app", embed_link="ytlink", video_link="link", github_repo="repo")
        Project.objects.create(name="App", about="Great app", embed_link="ytlink", video_link="link", github_repo="repo")

        # Create blogs
        Blog.objects.create(name="Blog", about="Great blog", picture_link="mdlink", blog_link="link")
        Blog.objects.create(name="Blog", about="Great blog", picture_link="mdlink", blog_link="link")
        Blog.objects.create(name="Blog", about="Great blog", picture_link="mdlink", blog_link="link")
        Blog.objects.create(name="Blog", about="Great blog", picture_link="mdlink", blog_link="link")

        # Create certificates
        Certificate.objects.create(name="Certificate", picture_link="piclink", validation="link")
        Certificate.objects.create(name="Certificate", picture_link="piclink", validation="link")
        Certificate.objects.create(name="Certificate", picture_link="piclink", validation="link")

        # Create Book
        Book.objects.create(title="Title", about="About", book_cover="piclink", link="link")
    
    def test_index(self):
        response = c.get("/")
        self.assertEqual(response.context["projects"].count(), 4)
        self.assertEqual(response.context["blogs"].count(), 4)
        self.assertEqual(response.context["certificates"].count(), 3)
        self.assertEqual(response.status_code, 200)

    def test_valid_add_question(self):
        response = c.post("/question/add",
            {"name": "Foo", "question": "What's your name?"},
            content_type="application/json",
            json_encoder=json.decoder
        )

        self.assertEqual(response.status_code, 200)

    def test_invalid_add_question(self):

        try:
            response = c.post("/question/add",
                {},
                content_type="application/json",
                json_encoder=json.decoder, raise_request_exception= False
            )
            raise IntegrityError
        except IntegrityError:
            self.assertRaises(IntegrityError)
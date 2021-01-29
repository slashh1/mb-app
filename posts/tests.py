from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Post
class PostModelTest(TestCase):

    def setup(self):
        Post.objects.create(text='just a text')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{Post.text}'
        self.assertEqual(expected_object_name,'just a test')
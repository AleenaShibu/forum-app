from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(test ="testing creating a post")
	def text_textContents(self):
		Post = Post.objects.get(id=1)
		expected_object_name =f'{ post.text }'
		self.assertEqual(expected_object_name,"testing creating a post")
# Create your tests here.

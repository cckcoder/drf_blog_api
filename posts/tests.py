from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create User
        testuser1 = User.objects.create_user(
            username="testuser1",
            password="abc1233"
        )
        testuser1.save()
        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1,
            title="Simple blog",
            body="just body content"
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Simple blog')
        self.assertEqual(body, 'just body content')





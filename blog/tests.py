from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class BlogTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests is Trues is equal to True. Should always pass. """ 
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Post. """
        user = User()
        user.save()

        post = Post(title="My Test Page", content="test", author=user)
        post.save()

        self.assertEqual(post.slug, "my-test-page")

class PostListViewTests(TestCase):
    def test_multiple_posts(self):
        user = User.objects.create()

        Post.objects.create(title="My Test Post", content="test", author=user)
        Post.objects.create(title="Other", content="test", author=user)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQueryEqual(
            responses, 
            ['<Post: My Test Page', '<Post:Other'],
            ordered=False
        )


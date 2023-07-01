from django.test import TestCase
from django.contrib.auth.models import User
from .models import Review


class TestReviewModel(TestCase):
    """
    Unit Tests For Review Model
    """
    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.review = Review.objects.create(
            author=self.user, rating=4, comment='Great product!'
        )

    def test_str_method(self):
        """
        Unit test for __str__ method
        """
        expected_str = f'Review by {self.user.username}'
        self.assertEqual(str(self.review), expected_str)

    def test_likes_count(self):
        """
        Unit test for likes count
        """
        self.assertEqual(self.review.likes_count(), 0)

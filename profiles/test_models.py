from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class TestProfileModel(TestCase):
    """
    Unit Tests for Profile model
    """
    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.profile, _ = Profile.objects.get_or_create(user=self.user)

    def test_str_method(self):
        """
        Unit test for __str__ method
        """
        self.assertEqual(str(self.profile), self.user.username)

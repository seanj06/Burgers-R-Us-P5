from django.test import TestCase
from django.contrib.auth.models import User
from .models import ContactMessage


class TestContactModel(TestCase):
    """
    Unit Tests for contact model
    """

    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_contact_message_str__(self):
        """
        Unit Test for testing __str__ method
        """
        contact_message = ContactMessage.objects.create(
            user=self.user,
            name='John test',
            email='johntest@test.com',
            subject='Test Subject',
            message='Test Message',
            issue='General Inquiry'
        )

        expected_string = f"General Inquiry by {self.user}"
        self.assertEqual(str(contact_message), expected_string)

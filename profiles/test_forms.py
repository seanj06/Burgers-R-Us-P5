from django.test import TestCase
from .models import Profile
from .forms import ProfileForm


class ProfileFormTest(TestCase):
    """
    Unit tests for profile form
    """
    def test_profile_form(self):
        """
        Unit test with profile data
        """
        form_data = {
            'default_phone_number': '1234567890',
            'default_eircode': 'D01AB12',
            'default_email': 'test@example.com',
            'default_town': 'Test Town',
            'default_address_1': 'Test Address 1',
            'default_address_2': 'Test Address 2',
            'default_address_3': 'Test Address 3',
            'default_county': 'Test County',
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

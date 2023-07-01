from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Profile
from checkout.models import Order


class TestProfileView(TestCase):
    """
    Unit Tests for Profile view
    """
    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.client = Client()

    def test_profile_view(self):
        """
        Unit test for response code and status
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)
        self.assertIsNotNone(response.context['form'])

    def test_profile_view_post_valid_form(self):
        """
        Test for valid form data
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile'), {
            'default_phone_number': '1234567890',
            'default_address_1': 'Test Address 1',
            'default_address_2': 'Test Address 2',
            'default_address_3': 'Test Address 3',
            'default_email': 'test@example.com',
            'default_eircode': 'EIR123',
            'default_town': 'Test Town',
            'default_county': 'Test County',
        })

        self.assertEqual(response.status_code, 200)
        updated_profile = get_object_or_404(Profile, user=self.user)
        self.assertEqual(updated_profile.default_phone_number, '1234567890')
        self.assertEqual(updated_profile.default_address_1, 'Test Address 1')
        self.assertEqual(updated_profile.default_address_2, 'Test Address 2')
        self.assertEqual(updated_profile.default_address_3, 'Test Address 3')
        self.assertEqual(updated_profile.default_email, 'test@example.com')
        self.assertEqual(updated_profile.default_eircode, 'EIR123')
        self.assertEqual(updated_profile.default_town, 'Test Town')
        self.assertEqual(updated_profile.default_county, 'Test County')

    def test_profile_view_invalid_form(self):
        """
        Unit test with invalid form data
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile'), {
            'default_email': 'invalid_email',
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertFalse(form.is_valid())
        self.assertContains(
            response, 'Sorry something went wrong', status_code=200
            )


class TestOrderHistory(TestCase):
    """
    Unit Tests For order history view
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.order = Order.objects.create(
            order_number='12345678', user_profile=self.profile,
            delivery_time='17:30'
            )

    def test_order_history_view(self):
        """
        Unit tests for order history view
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            reverse('order_history',
                    kwargs={'order_number': self.order.order_number})
            )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(
            response, f'This is a past confirmation for order number\
                 {self.order.order_number}.')
        self.assertContains(
            response, 'A confirmation email was sent on the order date.'
            )
        self.assertEqual(response.context['order'], self.order)
        self.assertTrue(response.context['from_profile'])

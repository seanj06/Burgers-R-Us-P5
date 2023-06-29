from django.test import TestCase
from .forms import OrderForm
from datetime import datetime, timedelta
from .delivery_times import generate_delivery_time_choices


class TestOrderForm(TestCase):
    """
    Unit Tests for OrderForm
    """

    def test_order_form_required_fields(self):
        form = OrderForm()
        self.assertTrue(form.fields['full_name'].required)
        self.assertTrue(form.fields['email'].required)
        self.assertTrue(form.fields['eircode'].required)
        self.assertTrue(form.fields['phone_number'].required)
        self.assertTrue(form.fields['county'].required)
        self.assertTrue(form.fields['town'].required)
        self.assertTrue(form.fields['address_1'].required)
        self.assertTrue(form.fields['delivery_time'].required)

    def test_order_form_valid_data(self):
        """
        Unit Test to check data is validated properly on form
        """
        delivery_date = datetime.now().date() + timedelta(days=1)
        choices = generate_delivery_time_choices(delivery_date)
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'eircode': '12345',
            'phone_number': '1234567890',
            'county': 'Test County',
            'town': 'Test Town',
            'address_1': 'Test Address 1',
            'delivery_time': choices[0][0],
        }
        form = OrderForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
        self.assertEqual(form.cleaned_data['full_name'], 'Test User')

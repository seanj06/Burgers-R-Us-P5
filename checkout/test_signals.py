from django.test import TestCase
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Order, OrderItem
from products.models import Food
from django.contrib.auth.models import User


class TestSignals(TestCase):
    """
    Unit Tests for signals
    """

    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.order = Order.objects.create(
            user_profile=self.user.profile,
            full_name='john test',
            phone_number='1234567890',
            email='johntest@example.com',
            eircode='EIR123',
            county='County',
            town='Town',
            address_1='Address 1',
            delivery_time='10:00',
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            food=Food.objects.create(name='Test Food', price=10),
            quantity=2
        )

    def test_update_on_delete(self):
        """
        Unit Test for update_on_delete method
        """
        self.order_item.delete()
        updated_order = Order.objects.get(pk=self.order.pk)
        self.assertEqual(updated_order.order_total, 0)

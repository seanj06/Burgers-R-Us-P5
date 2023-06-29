from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order, OrderItem
from products.models import Food
from profiles.models import Profile


class TestOrderModel(TestCase):
    """
    Unit Tests For Order model
    """
    def setUp(self):
        """
        setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.food = Food.objects.create(name='Test Food', price=10)
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

    def test_generate_order_number(self):
        """
        unit test for generate_order_number method
        """
        order_number = self.order._generate_order_number()
        self.assertIsNotNone(order_number)
        self.assertIsInstance(order_number, str)

    def test_update_total(self):
        """
        unit test for update_total method
        """
        self.order.order_item.create(food=self.food, quantity=2)
        self.order.update_total()
        self.assertEqual(self.order.order_total, 20)
        self.assertEqual(self.order.delivery_cost, 0)
        self.assertEqual(self.order.grand_total, 20)

    def test_save(self):
        """
        unit test for save method
        """
        order = Order(
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
        order.save()
        self.assertIsNotNone(order.order_number)
        self.assertIsInstance(order.order_number, str)

    def test_str_(self):
        """
        unit test for __str__ method
        """
        order_item = OrderItem(order=self.order, food=self.food, quantity=2)
        self.assertEqual(
            str(order_item),
            f'SKU {self.food.sku} on order {self.order.order_number}'
            )


class TestOrderItemModel(TestCase):
    """
    Unit Tests For Order model
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.food = Food.objects.create(name='Test Food', price=10)
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

    def test_str_(self):
        """
        unit test for __str__ method
        """
        order_item = OrderItem(order=self.order, food=self.food, quantity=2)
        self.assertEqual(
            str(order_item),
            f'SKU {self.food.sku} on order {self.order.order_number}'
        )

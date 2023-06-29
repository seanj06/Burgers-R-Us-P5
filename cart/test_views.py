from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from products.models import Food


class TestCartHome(TestCase):
    """
    Unit Test for cart_home view
    """
    def setUp(self):
        """
        Setup method
        """
        self.url = reverse('cart_home')
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_cart_home_view(self):
        """
        Test for view
        """
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'cart/cart.html')


class TestAddToCart(TestCase):
    """
    Unit Test for add_to_cart view
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.product = Food.objects.create(name='Test Food', price=10)

    def test_add_to_cart_view(self):
        """
        Test for view
        """
        self.client.login(username='testuser', password='testpassword')

        item_id = self.product.pk
        quantity = 2
        redirect_url = reverse('cart_home')

        response = self.client.post(reverse('add_to_cart', args=[item_id]), {
            'quantity': quantity,
            'redirect_url': redirect_url
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart.get(str(item_id)), quantity)


class TestEditCart(TestCase):
    """
    Unit Test for edit_cart view
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.product = Food.objects.create(name='Test Food', price=10)
        self.cart = {'1': 2}
        self.client.session['cart'] = self.cart

    def test_edit_cart_view(self):
        """
        Test for view
        """
        self.client.login(username='testuser', password='testpassword')
        item_id = self.product.pk
        quantity = 3
        response = self.client.post(reverse('edit_cart', args=[item_id]),
                                    {'quantity': quantity}
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('cart_home'))
        updated_cart = self.client.session.get('cart', {})
        self.assertEqual(updated_cart.get(str(item_id)), quantity)


class TestRemoveFromCart(TestCase):
    """
    Unit Test for remove_from_cart view
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.product = Food.objects.create(name='Test Food', price=10)
        self.cart = {'1': 2}
        self.client.session['cart'] = self.cart

    def test_remove_from_cart_view(self):
        """
        Test for view
        """
        self.client.login(username='testuser', password='testpassword')
        item_id = self.product.pk
        response = self.client.post(reverse(
            'remove_from_cart', args=[item_id]
            ))
        self.assertEqual(response.status_code, 200)
        updated_cart = self.client.session.get('cart', {})
        self.assertNotIn(str(item_id), updated_cart)

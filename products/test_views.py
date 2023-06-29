from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Food, Category, SubCategory
from .views import all_products


class TestAllProductsView(TestCase):
    """
    Unit tests for all products view
    """

    def setUp(self):
        """
        setup method
        """
        self.category = Category.objects.create(name='Test Category')
        self.subcategory = SubCategory.objects.create(name='Test Subcategory')
        self.food1 = Food.objects.create(
            name='Food 1', category=self.category,
            price=9.99
            )
        self.food2 = Food.objects.create(
            name='Food 2', category=self.category,
            sub_category=self.subcategory, price=8.99,
            )
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_all_products_no_filters(self):
        """
        Unit test for product view with no search filters
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.food1, response.context['products'])

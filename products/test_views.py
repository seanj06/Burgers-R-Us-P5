from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Food, Category, SubCategory
from .forms import ProductForm
from django.test.client import Client
from .views import all_products
from django.contrib.messages import get_messages
from decimal import Decimal
import re


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

    def test_all_products_with_search_filter(self):
        """
        Unit test for product view with search filter
        """
        response = self.client.get('/products/', {'q': 'Food 1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.food1, response.context['products'])
        self.assertNotIn(self.food2, response.context['products'])


class TestProductDetailView(TestCase):
    """
    Unit tests for product detail view
    """

    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.product = Food.objects.create(name='Test Product', price=9.99)

    def test_product_detail_view(self):
        """
        Test product detail view
        """
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.context['product'], self.product)


class TestAddProductView(TestCase):
    """
    Unit tests for add_product view
    """

    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

        self.category = Category.objects.create(name='Test Category')
        self.subcategory = SubCategory.objects.create(name='Test Subcategory')

    def test_add_product_view_with_authenticated_superuser(self):
        """
        Test add_product view with an authenticated superuser
        """
        self.client.force_login(self.user)

        form_data = {
            'category': self.category.id,
            'sub_category': self.subcategory.id,
            'name': 'Test Product',
            'description': 'Test description',
            'is_vegetarian': True,
            'is_gluten_free': True,
            'price': 9.99,
            'image_url': 'https://example.com/image.jpg',
            'is_available': True,
            'contains': ['Nuts', 'Dairy'],
        }
        response = self.client.post(reverse('add_product'), data=form_data)

        self.assertRedirects(response, reverse('products'))
        self.assertEqual(Food.objects.count(), 1)
        product = Food.objects.first()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Test description')
        self.assertEqual(product.is_vegetarian, True)
        self.assertEqual(product.is_gluten_free, True)
        self.assertEqual(product.price, Decimal('9.99'))
        self.assertEqual(product.image_url, 'https://example.com/image.jpg')
        self.assertEqual(product.is_available, True)
        self.assertEqual(list(product.contains), ['Nuts', 'Dairy'])
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully added product!')

    def test_add_product_view_with_invalid_form(self):
        """
        Test add_product view with an invalid form submission
        """
        self.client.force_login(self.user)

        form_data = {
            'name': 'Test Product',
        }
        response = self.client.post(reverse('add_product'), data=form_data)
        self.assertTemplateUsed(response, 'products/add_product.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        # Regex needed for test to pass
        self.assertRegex(
            str(messages[0]),
            r'Please\s+ensure\s+the\s+form\s+is\s+valid.'
             )

        # Assert that no product was added
        self.assertEqual(Food.objects.count(), 0)

    def test_add_product_view_with_unauthorized_user(self):
        """
        Test add_product view with an unauthorized user
        """
        user = User.objects.create_user(
            username='test', password='testpassword'
            )
        self.client.force_login(user)

        form_data = {
            'category': self.category.id,
            'sub_category': self.subcategory.id,
            'name': 'Test Product',
            'description': 'Test description',
            'is_vegetarian': True,
            'is_gluten_free': True,
            'price': 9.99,
            'image_url': 'https://example.com/image.jpg',
            'is_available': True,
            'contains': ['Nuts', 'Dairy'],
        }
        response = self.client.post(reverse('add_product'), data=form_data)
        self.assertRedirects(response, reverse('home'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Sorry you are not authorized to edit a product'
            )
        self.assertEqual(Food.objects.count(), 0)


class TestEditProductView(TestCase):
    """
    Unit tests for edit_product view
    """

    def setUp(self):
        """
        setup method
        """
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.subcategory = SubCategory.objects.create(name='Test Subcategory')
        self.product = Food.objects.create(
            name='Food 1', category=self.category, price=9.99
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
            )
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

    def test_edit_product_view_with_authenticated_superuser(self):
        """
        Test edit_product view with an authenticated superuser
        """
        self.client.force_login(self.superuser)

        form_data = {
            'name': 'Updated Product',
            'description': 'Updated description',
            'price': 19.99,
            'is_available': False,
        }
        response = self.client.post(
            reverse('edit_product', args=[self.product.id]), data=form_data
            )

        self.assertRedirects(
            response, reverse('product_detail', args=[self.product.id])
            )
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.description, 'Updated description')
        self.assertEqual(self.product.price,  Decimal('19.99'))
        self.assertEqual(self.product.is_available, False)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully updated product!')

    def test_edit_product_view_with_invalid_form(self):
        """
        Test edit_product view with invalid form data
        """
        self.client.force_login(self.superuser)

        form_data = {
            'name': 'test1',
            'description': 'Updated description',
            'price': 19.9999,
            'is_available': False,
        }
        response = self.client.post(
            reverse('edit_product', args=[self.product.id]), data=form_data
            )

        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to update product.\
                            Please ensure the form is valid.')

    def test_edit_product_view_unauthorized_user(self):
        """
        Test edit_product view with an unauthorized user
        """
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('edit_product', args=[self.product.id])
            )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Sorry you are not authorized to edit a product'
        )


class TestDeleteProductView(TestCase):
    """
    Unit tests for delete_product view
    """
    def setUp(self):
        """
        setup method
        """
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.subcategory = SubCategory.objects.create(name='Test Subcategory')
        self.product = Food.objects.create(
            name='Food 1', category=self.category, price=9.99
        )
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
            )
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )

    def test_delete_product_view_with_authenticated_superuser(self):
        """
        Test delete_product view with an authenticated superuser
        """
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse('delete_product', args=[self.product.id])
        )

        self.assertRedirects(response, reverse('products'))
        self.assertFalse(Food.objects.filter(pk=self.product.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product deleted!')

    def test_delete_product_view_unauthorized_user(self):
        """
        Test delete_product view with an unauthorized user
        """
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('delete_product', args=[self.product.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Food.objects.filter(pk=self.product.id).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Sorry you are not authorized to delete a product'
        )

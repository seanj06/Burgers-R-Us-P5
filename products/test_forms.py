from django.test import TestCase
from .forms import ProductForm
from .models import Category, SubCategory
from decimal import Decimal


class TestProductForm(TestCase):
    """
    Unit Tests for product form
    """
    def setUp(self):
        """
        setup method
        """
        self.category = Category.objects.create(name=' Test Category')
        self.sub_category = SubCategory.objects.create(
            name='Test Sub Category'
            )

    def test_product_form(self):
        form_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'category': self.category.id,
            'sub_category': self.sub_category.id,
            'price': 9.99,
        }
        form = ProductForm(data=form_data, files={})

        self.assertTrue(form.is_valid())
        product = form.save()

        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.sub_category, self.sub_category)
        self.assertEqual(product.price, Decimal('9.99'))

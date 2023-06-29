from django.test import TestCase
from .models import Category, SubCategory, Food


class TestCategoryModel(TestCase):
    """
    Unit Tests for Category model
    """
    def setUp(self):
        """
        setup method
        """
        self.category = Category.objects.create(name='Category')

    def test_str(self):
        """
        Unit test for testing __str__ method
        """
        category_str = str(self.category)
        self.assertEqual(category_str, self.category.name)


class TestSubCategoryModel(TestCase):
    """
    Unit Tests for Sub Category model
    """
    def setUp(self):
        """
        setup method
        """
        self.sub_category = SubCategory.objects.create(name='SubCategory')

    def test_str(self):
        """
        Unit test for testing __str__ method
        """
        sub_category_str = str(self.sub_category)
        self.assertEqual(sub_category_str, self.sub_category.name)


class TestFoodModel(TestCase):
    """
    Unit Tests for Food model
    """
    def setUp(self):
        """
        setup method
        """
        self.food = Food.objects.create(name='Test Food', price=9.99)

    def test_str(self):
        """
        Unit test for testing __str__ method
        """
        food_str = str(self.food)
        self.assertEqual(food_str, self.food.name)

from django.test import TestCase, Client
from django.urls import reverse
from .views import index


class TestIndexView(TestCase):
    """
    Unit Tests for home views
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()

    def test_index_view(self):
        """
        Unit test for index view
        """
        url = reverse('home')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

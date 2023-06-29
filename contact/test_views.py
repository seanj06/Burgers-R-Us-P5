from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ContactMessage
from .forms import ContactMessageForm


class TestContactViews(TestCase):
    """
    Unit tests for contact views
    """
    def setUp(self):
        """
        setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_contact_view(self):
        """
        Unit Test for contact view
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactMessageForm)

    def test_contact_view_valid_form(self):
        """
        Unit Test for contact valid form view
        """
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'name': 'john test',
            'email': 'johntest@test.com',
            'subject': 'Test Subject',
            'message': 'Test Message',
            'issue': 'Other',
        }
        form = ContactMessageForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('contact'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact_success'))
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.user, self.user)
        self.assertEqual(contact_message.subject, 'Test Subject')
        self.assertEqual(contact_message.message, 'Test Message')

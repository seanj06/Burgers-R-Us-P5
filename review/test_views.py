from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Review
from review.forms import ReviewForm
from .views import reviews
from django.contrib import messages


class TestReviewViews(TestCase):
    """
    Unit tests for review view
    """
    def setUp(self):
        """
        Setup method
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_reviews_view(self):
        """
        Unit test for review view and pagination
        """
        reviews_list = []
        for i in range(10):
            review = Review.objects.create(
                author=self.user, rating=5, comment=f'Test review {i + 1}'
            )
            reviews_list.append(review)

        response = self.client.get('/review/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review/review.html')
        self.assertEqual(
            [str(review) for review in response.context['reviews']],
            [str(review) for review in reviews_list[:6]]
        )


class TestReviewLikes(TestCase):
    """
    Unit Tests for review likes
    """
    def setUp(self):
        """
        Setup Method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.review = Review.objects.create(
            author=self.user, rating=5, comment='Test review'
            )

    def test_like_review(self):
        """
        Unit test for liking review
        """
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('like_review'), data={'review_id': self.review.id},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'likes_count': 1})

    def test_dislike_review(self):
        """
        Unit test for disliking review
        """
        self.client.force_login(self.user)
        self.review.likes.add(self.user)
        response = self.client.post(
            reverse('like_review'), data={'review_id': self.review.id},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
            )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'likes_count': 0})

    def test_invalid_request(self):
        """
        Unit test for correct json response
        """
        response = self.client.get(reverse('like_review'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{}')


class TestAddReview(TestCase):
    """
    Unit tests for add review view
    """
    def setUp(self):
        """
        Setup method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )

    def test_add_review(self):
        """
        Unit tests for add review
        """
        self.client.force_login(self.user)
        form_data = {'rating': 5, 'comment': 'Test review'}
        response = self.client.post(
            reverse('add_review'), data=form_data, follow=True
            )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('reviews'))
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.author, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Test review')
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(messages[0].message, 'Your review has been created')


class TestDeleteReview(TestCase):
    """
    Unit Tests For delete review view
    """
    def setUp(self):
        """
        Setup Method
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.review = Review.objects.create(
            author=self.user, rating=5, comment='Test review'
            )

    def test_delete_review(self):
        """
        unit test for delete review view
        """
        self.client.force_login(self.user)
        response = self.client.post(
            f'/review/delete/{self.review.id}/', follow=True
            )
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/review/')
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(messages[0].message, 'Your review has been deleted')

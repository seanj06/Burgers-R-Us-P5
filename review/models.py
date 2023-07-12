from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    """
    Model for User Reviews
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_reviews')

    class Meta:
        """
        Orders reviews by newly created
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns string with review author
        """
        return f'Review by {self.author.username}'

    def likes_count(self):
        """
        Returns total likes count on review
        """
        return self.likes.count()

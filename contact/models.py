from django.db import models
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    """
    Model for user contact
    """

    ISSUE_CHOICES = (
        ('General Inquiry', 'General Inquiry'),
        ('Issue With Food Order', 'Issue With Food Order'),
        ('Billing Question', 'Billing Question'),
        ('Food Not Delivered', 'Food Not Delivered'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    issue = models.CharField(max_length=100, choices=ISSUE_CHOICES, null=True)

    def __str__(self):
        return f"{self.issue} by {self.user}"

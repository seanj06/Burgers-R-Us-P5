from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Rating',
            'comment': 'Comment'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5})
        }

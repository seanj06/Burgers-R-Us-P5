from django.shortcuts import render, get_object_or_404
from .models import Review

# Create your views here.


def reviews(request):
    """
    View to render a list of all reviews
    """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'review/review_list.html', context)

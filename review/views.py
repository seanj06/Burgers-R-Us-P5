from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
    return render(request, 'review/review.html', context)


def like_review(request):
    """
    View for handling review like logic
    """
    if request.method == "POST" and request.is_ajax():
        review_id = request.POST.get("review_id")
        review = get_object_or_404(Review, id=review_id)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        # Return the updated like count
        likes_count = review.likes_count()
        return JsonResponse({"likes_count": likes_count})
    else:
        return JsonResponse({}, status=400)


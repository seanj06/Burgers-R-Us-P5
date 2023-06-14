from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm

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


def add_review(request):
    """
    View for adding a review
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Your review has been created')
            return redirect('reviews')
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }
    return render(request, 'review/add_review.html', context)


@login_required
def delete_review(request, review_id):
    """
    View for deleting a review
    """
    review = get_object_or_404(Review, id=review_id)
    if review.author == request.user:
        review.delete()
        messages.success(request, 'Your review has been deleted')
    else:
        messages.error(request, 'You are not authorized to delete this review')
    return redirect('reviews')


@login_required
def edit_review(request, review_id):
    """
    View for editing a review
    """
    review = get_object_or_404(Review, id=review_id)
    if review.author == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your review has been updated')
                return redirect('reviews')
        else:
            form = ReviewForm(instance=review)
    else:
        messages.error(request, 'You are not authorized to edit this review')
        return redirect('reviews')

    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'review/edit_review.html', context)

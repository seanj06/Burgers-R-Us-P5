from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from checkout.models import Order


def profile(request):
    """
    View for handling logic for profile page
    """
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated')
        else:
            messages.error(request, 'Sorry something went wrong')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View for handling profile page order history logic
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number\
                 {order.order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

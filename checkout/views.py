from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import OrderItem, Order
from profiles.models import Profile
from profiles.forms import ProfileForm
from products.models import Food
from django.utils import timezone
from datetime import datetime, timedelta, date
from cart.contexts import cart_contents
from .delivery_times import generate_delivery_time_choices
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    delivery_choices = generate_delivery_time_choices(date.today())

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'eircode': request.POST['eircode'],
            'phone_number': request.POST['phone_number'],
            'county': request.POST['county'],
            'town': request.POST['town'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'address_3': request.POST['address_3'],
        }

        delivery_time = request.POST.get('delivery_time')
        if not delivery_time:
            messages.error(request, 'Sorry delivery is currently unavailable')
            return render(request, template, context)

        form_data['delivery_time'] = delivery_time

        order_form = OrderForm(form_data)
        if order_form.is_valid:
            order = order_form.save()

            for item_id, item_data in cart.items():
                try:
                    food = Food.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            food=food,
                            quantity=item_data,
                        )
                        order_item.save()

                except Food.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart \
                         wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart_home'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, "Your cart is empty")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'eircode': profile.default_eircode,
                    'phone_number': profile.default_phone_number,
                    'town': profile.default_town,
                    'address_1': profile.default_address_1,
                    'address_2': profile.default_address_2,
                    'address_3': profile.default_address_3,
                    'county': profile.default_county,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret if intent else None,
        'delivery_choices': delivery_choices,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_email': order.email,
                'default_eircode': order.eircode,
                'default_phone_number': order.phone_number,
                'default_town': order.town,
                'default_address1': order.address_1,
                'default_address2': order.address_2,
                'default_address3': order.address_3,
                'default_county': order.county,
            }

            user_profile_form = ProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your order has been placed \
        Your food will be with you shortly. \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')

    if 'cart' in request.session:
        del request.session['cart']

    subject = f'Order Confirmation - Order #{order.order_number}'
    from_email = 'burgers-r-us@example.com'
    to_email = [order.email]

    html_message = render_to_string('checkout/email/order_confirmation.html',
                                    {'order': order})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message,
              from_email, to_email,
              html_message=html_message)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

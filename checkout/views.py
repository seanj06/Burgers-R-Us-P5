from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import OrderItem
from cart.models import Food
from cart.contexts import cart_contents
import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'eircode': request.POST['eircode'],
            'county': request.POST['county'],
            'town': request.POST['town'],
            'address_1': request.POST['adress_1'],
            'address_2': request.POST['address_2'],
            'address_3': request.POST['address_3'],
            'delivery_time': request.POST['delivery_time'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid:
            order = order_form.save()

            for item_id, item_data in cart.items():
                try:
                    product = Food.objects.get(id=item_id)
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

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

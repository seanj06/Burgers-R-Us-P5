from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Food


# Create your views here.


def cart_home(request):
    """
    A view that renders the cart page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    View to add item to cart
    """
    product = get_object_or_404(Food, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} were added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """
    View to edit item in cart
    """
    product = get_object_or_404(Food, pk=item_id)
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))

    if item_id in cart:
        cart[item_id] = quantity
        request, f'Updated {product.name} quantity to {cart[item_id]}'

    request.session['cart'] = cart
    return redirect(reverse('cart_home'))


def remove_from_cart(request, item_id):
    """
    View to remove item from cart
    """
    product = get_object_or_404(Food, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]
        request, f'Removed {product.name} from your cart'

    request.session['cart'] = cart
    return HttpResponse(status=200)

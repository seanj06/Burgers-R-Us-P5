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
    quantity = request.POST.get('quantity', '').strip()
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Check if quantity is empty or contains only whitespace
    if not quantity:
        messages.error(request, 'Invalid quantity')
        return redirect(redirect_url)

    # Check if quantity is a valid integer greater than 0
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        messages.error(request, 'Invalid quantity')
        return redirect(redirect_url)

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} was added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """
    View to edit item in cart
    """
    product = get_object_or_404(Food, pk=item_id)
    quantity = request.POST.get('quantity', '').strip()
    cart = request.session.get('cart', {})

    # Check if quantity is empty or contains only whitespace
    if not quantity:
        messages.error(request, 'Invalid quantity')
        return redirect(reverse('cart_home'))

    # Check if quantity is a valid integer between 1 - 99
    try:
        quantity = int(quantity)
        if quantity <= 0 or quantity > 99:
            raise ValueError
    except ValueError:
        messages.error(request, 'Invalid quantity')
        return redirect(reverse('cart_home'))

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

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
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)

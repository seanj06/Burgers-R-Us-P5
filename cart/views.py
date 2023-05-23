from django.shortcuts import render, redirect, reverse, HttpResponse

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):
    """
    View to edit item in cart
    """
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))

    if item_id in cart:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('cart_home'))


def remove_from_cart(request, item_id):
    """
    View to remove item from cart
    """
    cart = request.session.get('cart', {})

    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return HttpResponse(status=200)

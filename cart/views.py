from django.shortcuts import render

# Create your views here.


def cart_home(request):
    """
    A view that renders the cart page
    """

    return render(request, 'cart/cart.html')

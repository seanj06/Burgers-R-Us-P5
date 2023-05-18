from django.shortcuts import render, get_object_or_404
from .models import Food

# Create your views here.


def all_products(request):

    products = Food.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Food, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

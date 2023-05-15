from django.shortcuts import render
from .models import Food

# Create your views here.


def all_products(request):

    products = Food.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

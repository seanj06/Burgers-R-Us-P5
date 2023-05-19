from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Food, Category, SubCategory
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def all_products(request):

    products = Food.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    subcategory = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "subcategory" in request.GET:
            subcategory = request.GET["subcategory"].split(",")
            products = products.filter(sub_category__name__in=subcategory)
            subcategory = SubCategory.objects.filter(name__in=subcategory)  

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search must not be blank")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query
                ) | Q(
                description__icontains=query
                )

            products = products.filter(queries)

            if not products:  
                messages.info(
                    request, "No products found matching your search."
                    )

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'subcategory': subcategory,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Food, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

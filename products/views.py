from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Food, Category, SubCategory
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """
    View to handle logic of all products page
    """
    products = Food.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    subcategory = None
    # If filter is sort
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if sortkey == 'subcategory':
                sortkey = 'sub_category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    # If filter search by categories or sub categories
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "subcategory" in request.GET:
            subcategory = request.GET["subcategory"].split(",")
            products = products.filter(sub_category__name__in=subcategory)
            subcategory = SubCategory.objects.filter(name__in=subcategory)
        # If search by keyword
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

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'subcategory': subcategory,
        'current_sorting': current_sorting,
        'on_product_page': True,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to handle logic of product detail page
    """
    product = get_object_or_404(Food, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry you are not authorized to edit a product'
                       )
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(request,
                           'Failed to add product.\
                            Please ensure the form is valid.'
                           )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'on_product_page': True,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry you are not authorized to edit a product'
                       )
        return redirect(reverse('home'))

    product = get_object_or_404(Food, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products'))
        else:
            messages.error(request,
                           'Failed to update product.\
                            Please ensure the form is valid.'
                           )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'on_product_page': True,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry you are not authorized to delete a product'
                       )
        return redirect(reverse('home'))

    product = get_object_or_404(Food, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

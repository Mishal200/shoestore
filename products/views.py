from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    products = Product.objects.filter(available=True)

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(brand__icontains=query)
        )

    return render(request, 'products/product_list.html', {
        'products': products
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {
        'products': products
    })

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
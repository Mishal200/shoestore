from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Wishlist


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(product=product)
    return redirect('wishlist_detail')


def wishlist_detail(request):
    wishlist_items = Wishlist.objects.all()
    return render(request, 'wishlist/wishlist_detail.html', {
        'wishlist_items': wishlist_items
    })


def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id)
    item.delete()
    return redirect('wishlist_detail')
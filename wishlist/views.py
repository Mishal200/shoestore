from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Wishlist


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('wishlist_detail')


@login_required
def wishlist_detail(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(request, 'wishlist/wishlist_detail.html', {
        'wishlist_items': wishlist_items
    })


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    item.delete()
    return redirect('wishlist_detail')
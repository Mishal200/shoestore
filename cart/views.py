from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product


@login_required
def cart_view(request):
    # Show only the logged-in user's cart items
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get existing cart item for this user and product
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    # If item already exists, increase quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    # Remove only the current user's cart item
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )
    cart_item.delete()

    return redirect('cart')


@login_required
def checkout(request):
    # Get only current user's cart items
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })
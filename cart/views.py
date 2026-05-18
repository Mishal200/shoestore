from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from products.models import Product


def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.subtotal() for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')


def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.subtotal() for item in cart_items)

    # Optional: clear cart after checkout
    # CartItem.objects.all().delete()

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })
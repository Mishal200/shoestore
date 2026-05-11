from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart_items = CartItem.objects.all()

    if not cart_items:
        return redirect('cart')

    total = sum(item.subtotal() for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

        # Reduce stock
        item.product.stock -= item.quantity
        item.product.save()

    # Clear cart
    cart_items.delete()

    return render(request, 'orders/order_success.html', {
        'order': order
    })
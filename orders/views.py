from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):
    # Your CartItem model does not have a user field,
    # so get all cart items.
    cart_items = CartItem.objects.all()

    # If cart is empty, redirect to cart page
    if not cart_items.exists():
        return redirect('cart')

    # Calculate total amount
    total = sum(item.subtotal() for item in cart_items)

    # Create order
    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        status='Pending'
        # order_number is generated automatically in Order.save()
    )

    # Create order items and update stock
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

    # Show success page
    return render(request, 'orders/order_success.html', {
        'order': order
    })


def track_order(request):
    order = None
    order_number = request.GET.get('order_number')

    if order_number:
        try:
            order = Order.objects.get(order_number=order_number)
        except Order.DoesNotExist:
            order = None

    return render(request, 'orders/track_order.html', {
        'order': order,
        'order_number': order_number,
    })
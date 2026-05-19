from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):
    
    cart_items = CartItem.objects.all()

   
    if not cart_items.exists():
        return redirect('cart')

   
    total = sum(item.subtotal() for item in cart_items)

   
    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        status='Pending'
        
    )

    
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

        
        item.product.stock -= item.quantity
        item.product.save()

    
    cart_items.delete()

   
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
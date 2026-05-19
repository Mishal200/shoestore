# cart/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class CartItem(models.Model):
    # Connect each cart item to a logged-in user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # Product added to cart
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Quantity of the product
    quantity = models.PositiveIntegerField(default=1)

    # Calculate subtotal
    def subtotal(self):
        return self.product.price * self.quantity

    # Display in admin panel
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
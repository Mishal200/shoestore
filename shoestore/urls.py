from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Products app (home page and product detail)
    path('', include('products.urls')),

    # Cart app
    path('cart/', include('cart.urls')),

    # Wishlist app
    path('wishlist/', include('wishlist.urls')),

    # Orders app (checkout and track order)
    path('orders/', include('orders.urls')),

    # Authentication (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
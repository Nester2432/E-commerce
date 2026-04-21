"""
config/urls.py
URLs raíz — incluye las rutas de cada app.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls", namespace="core")),
    path("catalogo/", include("apps.catalog.urls", namespace="catalog")),
    path("carrito/", include("apps.cart.urls", namespace="cart")),
    path("checkout/", include("apps.orders.urls", namespace="orders")),
    path("pagos/", include("apps.payments.urls", namespace="payments")),
]

# Servir media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

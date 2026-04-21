"""
apps/cart/context_processors.py
Hace el carrito disponible en todos los templates automáticamente.
"""

from .cart import Cart


def cart(request):
    return {"cart": Cart(request)}

"""
apps/cart/views.py
Vistas del carrito: agregar, eliminar, actualizar cantidades.
Responde JSON para interacciones AJAX y redirige para requests normales.
"""

import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt

from apps.catalog.models import VarianteProducto
from .cart import Cart


def cart_detail(request):
    """Vista del carrito de compras."""
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, "cart/cart_detail.html", context)


@require_POST
def cart_add(request):
    """
    Agrega una variante al carrito.
    Acepta POST con variante_id y cantidad.
    Responde JSON si es una request AJAX.
    """
    cart = Cart(request)
    variante_id = request.POST.get("variante_id")
    cantidad = int(request.POST.get("cantidad", 1))
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if not variante_id:
        if is_ajax:
            return JsonResponse({"ok": False, "error": "Variante no especificada."}, status=400)
        return redirect("cart:detail")

    variante = get_object_or_404(VarianteProducto, id=variante_id, activa=True)

    # Validar stock
    if variante.stock <= 0:
        if is_ajax:
            return JsonResponse({"ok": False, "error": "Producto sin stock."}, status=400)
        return redirect("catalog:product_detail", slug=variante.producto.slug)

    cart.agregar(variante, cantidad)

    if is_ajax:
        return JsonResponse({
            "ok": True,
            "cart_count": len(cart),
            "subtotal": str(cart.subtotal),
            "message": f'"{variante.producto.nombre}" agregado al carrito.',
        })

    return redirect("cart:detail")


@require_POST
def cart_remove(request):
    """Elimina una variante del carrito."""
    cart = Cart(request)
    variante_id = request.POST.get("variante_id")
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if variante_id:
        cart.eliminar(variante_id)

    if is_ajax:
        return JsonResponse({
            "ok": True,
            "cart_count": len(cart),
            "subtotal": str(cart.subtotal),
        })

    return redirect("cart:detail")


@require_POST
def cart_update(request):
    """Actualiza la cantidad de una variante en el carrito."""
    cart = Cart(request)
    variante_id = request.POST.get("variante_id")
    cantidad = request.POST.get("cantidad", 1)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    try:
        cantidad = int(cantidad)
    except (ValueError, TypeError):
        cantidad = 1

    if variante_id:
        cart.actualizar_cantidad(variante_id, cantidad)

    if is_ajax:
        # Calcular subtotal del ítem actualizado
        item_subtotal = "0"
        for item in cart:
            if str(item["variante_id"]) == str(variante_id):
                item_subtotal = str(item["subtotal"])
                break

        return JsonResponse({
            "ok": True,
            "cart_count": len(cart),
            "subtotal": str(cart.subtotal),
            "item_subtotal": item_subtotal,
        })

    return redirect("cart:detail")

"""
apps/cart/cart.py
Clase Cart: maneja el carrito de compras en sesión de Django.
No requiere base de datos — todo vive en la sesión del usuario.
"""

from decimal import Decimal
from django.conf import settings
from apps.catalog.models import VarianteProducto


CART_SESSION_ID = "cart"


class Cart:
    """
    Carrito de compras basado en sesión.

    Estructura en sesión:
    {
        "variante_id": {
            "cantidad": int,
            "precio": str,           # str para serialización JSON
            "nombre": str,
            "talle": str,
            "color": str,
            "slug": str,
            "imagen_url": str,
        },
        ...
    }
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def agregar(self, variante: VarianteProducto, cantidad: int = 1) -> None:
        """Agrega una variante al carrito o incrementa su cantidad."""
        variante_id = str(variante.id)

        if variante_id not in self.cart:
            imagen_url = ""
            if variante.producto.imagen_principal:
                try:
                    imagen_url = variante.producto.imagen_principal.imagen.url
                except Exception:
                    pass

            self.cart[variante_id] = {
                "cantidad": 0,
                "precio": str(variante.producto.precio),
                "nombre": variante.producto.nombre,
                "talle": variante.talle,
                "color": variante.color,
                "slug": variante.producto.slug,
                "imagen_url": imagen_url,
                "variante_id": variante_id,
            }

        # Validar que no exceda el stock disponible
        nueva_cantidad = self.cart[variante_id]["cantidad"] + cantidad
        if nueva_cantidad > variante.stock:
            nueva_cantidad = variante.stock

        self.cart[variante_id]["cantidad"] = nueva_cantidad
        self.guardar()

    def eliminar(self, variante_id: str) -> None:
        """Elimina una variante del carrito."""
        variante_id = str(variante_id)
        if variante_id in self.cart:
            del self.cart[variante_id]
            self.guardar()

    def actualizar_cantidad(self, variante_id: str, cantidad: int) -> None:
        """Actualiza la cantidad de una variante en el carrito."""
        variante_id = str(variante_id)
        if variante_id in self.cart:
            if cantidad <= 0:
                self.eliminar(variante_id)
            else:
                # Validar stock
                try:
                    variante = VarianteProducto.objects.get(id=variante_id)
                    cantidad = min(cantidad, variante.stock)
                except VarianteProducto.DoesNotExist:
                    self.eliminar(variante_id)
                    return
                self.cart[variante_id]["cantidad"] = cantidad
                self.guardar()

    def limpiar(self) -> None:
        """Vacía el carrito."""
        del self.session[CART_SESSION_ID]
        self.session.modified = True

    def guardar(self) -> None:
        """Marca la sesión como modificada para que Django la persista."""
        self.session.modified = True

    def __iter__(self):
        """Itera sobre los ítems del carrito enriquecidos con objetos Producto."""
        variante_ids = self.cart.keys()
        variantes = VarianteProducto.objects.filter(
            id__in=variante_ids
        ).select_related("producto")

        cart = self.cart.copy()
        for variante in variantes:
            cart[str(variante.id)]["variante"] = variante

        for item in cart.values():
            item["precio"] = Decimal(item["precio"])
            item["subtotal"] = item["precio"] * item["cantidad"]
            yield item

    def __len__(self) -> int:
        """Devuelve la cantidad total de ítems (unidades) en el carrito."""
        return sum(item["cantidad"] for item in self.cart.values())

    @property
    def subtotal(self) -> Decimal:
        """Subtotal sin envío."""
        return sum(
            Decimal(item["precio"]) * item["cantidad"]
            for item in self.cart.values()
        )

    @property
    def esta_vacio(self) -> bool:
        return len(self) == 0

    def get_total_con_envio(self, costo_envio: Decimal = Decimal("0")) -> Decimal:
        return self.subtotal + costo_envio

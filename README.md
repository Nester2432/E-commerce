# Tienda de Ropa — Arquitectura del Proyecto

## Estructura de carpetas

```
tienda_ropa/
│
├── config/                         # Configuración central del proyecto
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py                 # Settings compartidos
│   │   ├── local.py                # Settings de desarrollo
│   │   └── production.py          # Settings de producción
│   ├── urls.py                     # URLs raíz
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/
│   ├── core/                       # Funcionalidades transversales
│   │   ├── models.py               # Modelos base (TimeStampedModel)
│   │   ├── views.py                # Home, búsqueda general
│   │   ├── urls.py
│   │   └── templatetags/           # Tags personalizados
│   │
│   ├── catalog/                    # Catálogo de productos
│   │   ├── models.py               # Categoria, Producto, Variante, Imagen
│   │   ├── views.py                # Listado, detalle, filtros
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── forms.py                # Formulario de filtros/búsqueda
│   │
│   ├── cart/                       # Carrito de compras (sesión)
│   │   ├── cart.py                 # Clase Cart con lógica de sesión
│   │   ├── views.py                # Agregar, quitar, actualizar
│   │   ├── urls.py
│   │   └── context_processors.py  # Cart disponible en todos los templates
│   │
│   ├── orders/                     # Pedidos
│   │   ├── models.py               # Pedido, ItemPedido
│   │   ├── views.py                # Checkout, confirmación
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── forms.py                # Formulario de checkout
│   │
│   ├── payments/                   # Pagos con Mercado Pago
│   │   ├── models.py               # Pago
│   │   ├── views.py                # Crear preferencia, webhook
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── services.py             # Integración MP (lógica aislada)
│   │
│   ├── shipping/                   # Envíos con Andreani
│   │   ├── models.py               # Envio, TrackingEvento
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── services.py             # Integración Andreani (lógica aislada)
│   │
│   └── customers/                  # Clientes y direcciones
│       ├── models.py               # Cliente, DireccionEnvio
│       ├── views.py
│       ├── urls.py
│       ├── admin.py
│       └── forms.py
│
├── templates/
│   ├── base.html                   # Layout base con navbar y footer
│   ├── includes/
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   └── messages.html
│   ├── core/
│   │   └── home.html
│   ├── catalog/
│   │   ├── product_list.html
│   │   └── product_detail.html
│   ├── cart/
│   │   └── cart_detail.html
│   ├── orders/
│   │   ├── checkout.html
│   │   └── order_success.html
│   └── payments/
│       ├── payment_pending.html
│       └── payment_failed.html
│
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── components.css
│   │   ├── catalog.css
│   │   ├── cart.css
│   │   └── checkout.css
│   ├── js/
│   │   ├── cart.js
│   │   ├── catalog.js
│   │   └── checkout.js
│   └── images/
│
├── media/                          # Archivos subidos por usuarios
├── manage.py
└── requirements.txt
```

## Apps y responsabilidades

| App | Responsabilidad |
|-----|----------------|
| `core` | Home, búsqueda, modelos base, templatetags |
| `catalog` | Productos, categorías, variantes, filtros |
| `cart` | Carrito de sesión, lógica de items |
| `orders` | Pedidos, checkout, ítems de pedido |
| `payments` | Integración Mercado Pago, webhook, estados de pago |
| `shipping` | Integración Andreani, cotización, tracking |
| `customers` | Clientes, direcciones de envío |

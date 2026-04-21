"""
config/settings/local.py
Settings para entorno de desarrollo local.
"""

from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# ─── Base de datos local ─────────────────────────────────────────────────────

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tienda_ropa_db",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# ─── Email en consola durante desarrollo ─────────────────────────────────────

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ─── Modo sandbox para integraciones ─────────────────────────────────────────

MERCADOPAGO_SANDBOX = True
ANDREANI_SANDBOX = True

# ─── Django Debug Toolbar (opcional, descomentar si se instala) ───────────────

# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# INTERNAL_IPS = ["127.0.0.1"]

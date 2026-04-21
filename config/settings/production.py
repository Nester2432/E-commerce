"""
config/settings/production.py
Settings para entorno de producción.
"""

import os
from .base import *  # noqa

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# ─── Base de datos desde variable de entorno ─────────────────────────────────

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ.get("DB_PORT", "5432"),
        "CONN_MAX_AGE": 60,
    }
}

# ─── Seguridad ────────────────────────────────────────────────────────────────

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ─── Mercado Pago producción ──────────────────────────────────────────────────

MERCADOPAGO_ACCESS_TOKEN = os.environ.get("MP_ACCESS_TOKEN", "")
MERCADOPAGO_PUBLIC_KEY = os.environ.get("MP_PUBLIC_KEY", "")
MERCADOPAGO_WEBHOOK_SECRET = os.environ.get("MP_WEBHOOK_SECRET", "")
MERCADOPAGO_SANDBOX = False

# ─── Andreani producción ──────────────────────────────────────────────────────

ANDREANI_USERNAME = os.environ.get("ANDREANI_USERNAME", "")
ANDREANI_PASSWORD = os.environ.get("ANDREANI_PASSWORD", "")
ANDREANI_CLIENT_NUMBER = os.environ.get("ANDREANI_CLIENT_NUMBER", "")
ANDREANI_CONTRACT_NUMBER = os.environ.get("ANDREANI_CONTRACT_NUMBER", "")
ANDREANI_SANDBOX = False

# ─── Email ────────────────────────────────────────────────────────────────────

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# ─── Archivos estáticos (WhiteNoise o S3) ─────────────────────────────────────

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa

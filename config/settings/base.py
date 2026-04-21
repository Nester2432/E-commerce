"""
config/settings/base.py
Settings compartidos entre todos los entornos.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "django-insecure-change-this-in-production"

DEBUG = False

ALLOWED_HOSTS = []

# ─── Aplicaciones ───────────────────────────────────────────────────────────

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    # Agregar librerías externas aquí (ej. django-crispy-forms, pillow, etc.)
]

LOCAL_APPS = [
    "apps.core",
    "apps.catalog",
    "apps.cart",
    "apps.orders",
    "apps.payments",
    "apps.shipping",
    "apps.customers",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ─── Middleware ──────────────────────────────────────────────────────────────

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ─── Templates ───────────────────────────────────────────────────────────────

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Carrito disponible en todos los templates
                "apps.cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ─── Base de datos (PostgreSQL) ───────────────────────────────────────────────

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tienda_ropa_db",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
        "CONN_MAX_AGE": 60,
        "OPTIONS": {
            "connect_timeout": 10,
        },
    }
}

# ─── Validación de contraseñas ────────────────────────────────────────────────

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── Internacionalización ─────────────────────────────────────────────────────

LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# ─── Archivos estáticos y media ───────────────────────────────────────────────

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─── Sesiones ────────────────────────────────────────────────────────────────

SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 86400 * 7  # 7 días
SESSION_SAVE_EVERY_REQUEST = True

# ─── Mercado Pago ─────────────────────────────────────────────────────────────

MERCADOPAGO_ACCESS_TOKEN = ""          # Completar con credenciales reales
MERCADOPAGO_PUBLIC_KEY = ""            # Completar con credenciales reales
MERCADOPAGO_WEBHOOK_SECRET = ""        # Secret para validar webhooks
MERCADOPAGO_SANDBOX = True             # False en producción

# ─── Andreani ─────────────────────────────────────────────────────────────────

ANDREANI_USERNAME = ""                 # Completar con credenciales reales
ANDREANI_PASSWORD = ""                 # Completar con credenciales reales
ANDREANI_CLIENT_NUMBER = ""            # Número de cliente Andreani
ANDREANI_CONTRACT_NUMBER = ""          # Número de contrato
ANDREANI_BASE_URL = "https://api.andreani.com"
ANDREANI_SANDBOX = True                # False en producción

# ─── Email ────────────────────────────────────────────────────────────────────

DEFAULT_FROM_EMAIL = "noreply@tiendaropa.com"

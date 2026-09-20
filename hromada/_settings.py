"""
Django settings for hromada project.

Django settings.py for development.

Before setup:
1. Rename settings.py to __settings.py.
2. Rename _settings.py to settings.py.

Setup:
1. Create a virtual environment:
   python -m venv .venv
2. Activate the virtual environment:
   source .venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Generate and set the SECRET_KEY
5. Run the development server:
   python manage.py runserver

Next time:
1. Activate the virtual environment:
   source .venv/bin/activate
2. Run the development server:
   python manage.py runserver

When finished:
1. Stop the development server with Ctrl+C.
2. Deactivate the virtual environment:
   deactivate

After finishing:
1. Rename settings.py to _settings.py.
2. Rename __settings.py to settings.py.

TODO:
- Replace temporary settings renaming with proper environment configuration.
- Add Docker support for development, staging, and production.
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from django.contrib import staticfiles
from urllib.parse import urlparse
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

# dev: 1 | KEY
# -------------------------------------------------------------------------start
# SECRET_KEY = os.environ["SECRET_KEY"]
SECRET_KEY = ""
# ---------------------------------------------------------------------------end
# end dev: 1

# dev: 2 | DEBUG
# -------------------------------------------------------------------------start
# DEBUG = False
DEBUG = True
# ---------------------------------------------------------------------------end
# end dev: 2

# dev: 3 | HOSTS
# -------------------------------------------------------------------------start
# ALLOWED_HOSTS = ["hromada-b4df642e405d.herokuapp.com", "hromada.me", "www.hromada.me"]
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
# ---------------------------------------------------------------------------end
# end dev: 3

INSTALLED_APPS = [
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary",
    "cloudinary_storage",
    "ckeditor",
    "parler",
    "home.apps.HomeConfig",
    "project.apps.ProjectConfig",
    "create.apps.CreateConfig",
    "search.apps.SearchConfig",
    "wiki.apps.WikiConfig",
    "selfgov.apps.SelfgovConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hromada.urls"

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
                "hromada.context_processors.current_language_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "hromada.wsgi.application"

AUTH_USER_MODEL = "account.User"


# dev: 4 | DATABASE
# -------------------------------------------------------------------------start
# jawsdb_url = os.environ.get("JAWSDB_URL")
# DATABASE_URL = os.environ["JAWSDB_URL"]

# if jawsdb_url:
#     url = urlparse(jawsdb_url)

#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.mysql",
#             "NAME": url.path[1:],
#             "USER": url.username,
#             "PASSWORD": url.password,
#             "HOST": url.hostname,
#             "PORT": url.port,
#             "OPTIONS": {
#                 "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
#                 "charset": "utf8mb4",
#             },
#         }
#     }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# ---------------------------------------------------------------------------end
# end dev 4

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGES = [
    ("en", _("English")),
    ("ua", _("Українська")),
    ("ru", _("Русский")),
    ("ct", _("Qirimtatar")),
]

LANGUAGE_CODE = "ru"

PARLER_LANGUAGES = {
    None: (
        {"code": "en"},
        {"code": "ua"},
        {"code": "ru"},
        {"code": "ct"},
    ),
    "default": {
        "fallbacks": ["ru"],
        "hide_untranslated": False,
    },
}

TIME_ZONE = "Europe/Simferopol"

USE_I18N = True
USE_TZ = True
USE_L10N = True

LOCALE_PATHS = [BASE_DIR / "locale"]


STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = BASE_DIR / "staticfiles"

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# dev: 5 | CLOUDINARY
# -------------------------------------------------------------------------start
# CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# cloudinary.config(
#     cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
#     api_key=os.environ.get("CLOUDINARY_API_KEY"),
#     api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
#     secure=True,
# )
# ---------------------------------------------------------------------------end
# end dev: 5

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "account.User"

LOGIN_REDIRECT_URL = "home_page"
LOGOUT_REDIRECT_URL = "home_page"
LOGIN_URL = "login"
LOGOUT_URL = "logout"

# dev: 6 | EMAIL
# -------------------------------------------------------------------------start
# Email server configuration
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
# EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
# ---------------------------------------------------------------------------end
# end dev: 6

# CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "extraAllowedContent": "iframe[*]; img[*]; video[*]; source[*]; figure(*)",
        "removePlugins": "exportpdf",
        "extraPlugins": "image2,embed,autoembed",
    }
}

# dev: 7 | SECURITY
# -------------------------------------------------------------------------start
# Security
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# ---------------------------------------------------------------------------end
# end dev: 7

# Referrer
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

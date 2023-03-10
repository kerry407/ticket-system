from .base import *
import dj_database_url

DEBUG = False


ALLOWED_HOSTS = ["*"]

# Whitenoise settings for static files in production 
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Render PostgreSQL live database

DATABASES = {
    'default': dj_database_url.parse(config("DATABASE_URL"))
}
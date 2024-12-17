from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env.production")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if bool(os.getenv("DEBUG_PROD")) == False else True

ALLOWED_HOSTS = ["cmogujarat.gov.in","127.0.0.1", "10.10.2.179"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fellowshipbackendprod",
        "USER": "postgres",
        "PASSWORD": "cmoai",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

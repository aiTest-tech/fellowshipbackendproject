from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if bool(os.getenv("DEBUG_PROD")) == False else True

ALLOWED_HOSTS = ["10.10.2.179"]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

from .base import *
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env.staging")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if bool(os.getenv("DEBUG_PROD")) == False else True

ALLOWED_HOSTS = ["*"]
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("ENGINE"),
#         "NAME": os.getenv("NAME"),
#         "USER": os.getenv("USER"),
#         "PASSWORD": os.getenv("PASSWORD"),
#         "HOST": os.getenv("HOST"),
#         "PORT": os.getenv("PORT"),
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fellowshipbackendstaging",
        "USER": "postgres",
        # "PASSWORD": "cmo",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

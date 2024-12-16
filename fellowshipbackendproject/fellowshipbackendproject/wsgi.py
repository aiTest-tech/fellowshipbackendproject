import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Load the environment variables
load_dotenv()

# os.environ.setdefault(
#     "DJANGO_SETTINGS_MODULE",
#     os.getenv("DJANGO_SETTINGS_MODULE", "fellowshipbackendproject.settings.dev"),
# )

os.environ.setdefault("DJANGO_ENV", "dev")
environment = os.environ["DJANGO_ENV"]
print(f"==>> environment in wsgi application: {environment}")

if environment == "staging":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "fellowshipbackendproject.settings.staging"
    )
elif environment == "production":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "fellowshipbackendproject.settings.prod"
    )
else:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "fellowshipbackendproject.settings.dev"
    )

application = get_wsgi_application()

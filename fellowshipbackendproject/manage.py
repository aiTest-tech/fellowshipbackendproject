# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fellowshipbackendproject.settings")
# try:
#     from django.core.management import execute_from_command_line
# except ImportError as exc:
#     raise ImportError(
#         "Couldn't import Django. Are you sure it's installed and "
#         "available on your PYTHONPATH environment variable? Did you "
#         "forget to activate a virtual environment?"
#     ) from exc
# execute_from_command_line(sys.argv)


# if __name__ == "__main__":
#     main()


import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_ENV", "dev")
    environment = os.environ["DJANGO_ENV"]
    print(f"==>> environment: {environment}")

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

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

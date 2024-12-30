from django.contrib.admin.sites import AdminSite
from django.contrib.auth.views import LoginView
from django.urls import path
from .forms import AdminLoginFormWithCaptcha


class CustomAdminSite(AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "login/",
                LoginView.as_view(
                    template_name="admin/login.html",
                    authentication_form=AdminLoginFormWithCaptcha,
                ),
                name="login",
            ),
        ]
        return custom_urls + urls

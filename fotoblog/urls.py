from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)

from django.urls import path

import blog.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", blog.views.home, name="home"),
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            template_name="authentication/logout.html", next_page="login"
        ),
        name="logout",
    ),
    path(
        "change-password/",
        PasswordChangeView.as_view(
            template_name="authentication/password_change_form.html",
        ),
        name="password_change",
    ),
    path(
        "change-password-done/",
        PasswordChangeDoneView.as_view(
            template_name="authentication/password_change_done.html",
        ),
        name="password_change_done",
    ),
]

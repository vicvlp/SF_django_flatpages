from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.flatpages import views as flatpage_views
from django.urls import include, path
from django.views.generic import RedirectView

from fpages.views import private_flatpage

urlpatterns = [
    path("", RedirectView.as_view(url="/about/", permanent=False), name="home"),
    path("admin/", admin.site.urls),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    # Literal admin-only page. The FlatPage itself is also marked
    # registration_required=True in the data migration.
    path("private/", private_flatpage, name="private_flatpage"),
    # Remaining FlatPages: /about/ and /styled/
    path("", include("django.contrib.flatpages.urls")),
]

from django.contrib import admin
from django.urls import path, include  # Import `include` to link app URLs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("To_Do.urls")),  # Include URLs from the `to_do` app
]

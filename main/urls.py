from django.urls import URLPattern, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form/", views.form, name="form"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
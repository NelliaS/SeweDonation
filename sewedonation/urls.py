from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('registration', views.registration, name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
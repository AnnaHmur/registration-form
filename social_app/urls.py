from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login, name="login"),
    path("edit/", views.edit, name="edit"),
    path('all/', views.all_users, name='all_users'),
    path('', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

print(include('apps.receitas.urls'))

urlpatterns = [
    path('', include('apps.receitas.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

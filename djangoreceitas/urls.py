from django.contrib import admin
from django.urls import path, include

print(include('apps.receitas.urls'))

urlpatterns = [
    path('', include('apps.receitas.urls')),
    path('admin/', admin.site.urls),
]

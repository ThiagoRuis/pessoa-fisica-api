from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa_fisica/', include('pessoa_fisica.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ربط تطبيق API
    path('', include('pages.urls')),   # ربط تطبيق الصفحات
]
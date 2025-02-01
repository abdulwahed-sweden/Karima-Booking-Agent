from django.contrib import admin
from .models import Client, Translator

# تسجيل نموذج Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'language', 'punctuality_rating')  # الأعمدة التي ستظهر في لوحة التحكم
    search_fields = ('name', 'language')  # الحقول التي يمكن البحث فيها
    list_filter = ('priority', 'language')  # الفلاتر على الجانب الأيسر

# تسجيل نموذج Translator
@admin.register(Translator)
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'languages', 'accuracy_rating', 'speed_rating')  # الأعمدة التي ستظهر في لوحة التحكم
    search_fields = ('name', 'languages')  # الحقول التي يمكن البحث فيها
    list_filter = ('languages',)  # الفلاتر على الجانب الأيسر

from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('first_name', 'last_name', 'username', 'email')
    search_fields = ('first_name', 'last_name', 'username', 'email')



from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('first_name', 'last_name', 'username', 'email')
    search_fields = ('first_name', 'last_name', 'username', 'email')


from .models import OTP, PremiumUser

class OTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'is_verified')
    list_filter = ('user', 'otp', 'is_verified')
    search_fields = ('user', 'otp', 'is_verified')

class PremiumUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium', 'duration', 'price')
    list_filter = ('user', 'is_premium', 'duration', 'price')
    search_fields = ('user', 'is_premium', 'duration', 'price')

admin.site.register(OTP, OTPAdmin)

admin.site.register(PremiumUser, PremiumUserAdmin)
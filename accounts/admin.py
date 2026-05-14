from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ContractorProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'user_type', 'is_active']
    list_filter = ['user_type']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )


@admin.register(ContractorProfile)
class ContractorProfileAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'niche', 'service_area', 'is_verified']
    list_filter = ['niche', 'is_verified']
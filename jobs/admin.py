from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'niche', 'location', 'status', 'created_at']
    list_filter = ['niche', 'status']
    search_fields = ['title', 'location']
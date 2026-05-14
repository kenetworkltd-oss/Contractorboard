from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Inquiry, Review


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['job', 'contractor', 'status', 'sent_at']
    list_filter = ['status']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['contractor', 'homeowner', 'rating', 'created_at']

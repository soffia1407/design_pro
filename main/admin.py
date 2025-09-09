from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    list_editable = ['status']
    search_fields = ['title', 'user__username']
    readonly_fields = ['created_at']
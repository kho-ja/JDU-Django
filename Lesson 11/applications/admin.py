from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "file"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at"]

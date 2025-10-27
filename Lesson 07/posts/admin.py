from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "description_word_count")
    search_fields = ("title", "description")
    readonly_fields = ("created_at",)

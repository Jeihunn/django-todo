from django.contrib import admin
from .models import Todo, Favorite


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated_at", "created_at",
                    "user", "is_active", "is_completed", "slug"]
    list_editable = ["is_active", "is_completed"]
    list_display_links = ["id", "title"]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user"]

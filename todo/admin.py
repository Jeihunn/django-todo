from django.contrib import admin
from .models import List, Todo, Favorite


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated_at", "created_at",
                    "user", "is_active", "slug"]
    list_editable = ["is_active"]
    list_display_links = ["id", "title"]
    search_fields= ["title"]
    list_filter = ["is_active", "user"]


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated_at", "created_at",
                    "is_active", "is_completed", "is_deleted", "user", "list", "slug"]
    list_editable = ["is_active", "is_completed", "is_deleted"]
    list_display_links = ["id", "title"]
    search_fields= ["title"]
    list_filter = ["is_active", "is_completed", "is_deleted", "user", "list"]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ["user"]

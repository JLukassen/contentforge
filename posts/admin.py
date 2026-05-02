from django.contrib import admin

from .models import SocialPost


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "x_status",
        "reddit_status",
        "instagram_status",
        "created_at",
        "scheduled_for",
    )

    list_filter = (
        "category",
        "status",
        "x_status",
        "reddit_status",
        "instagram_status",
        "created_at",
        "scheduled_for",
    )

    search_fields = (
        "title",
        "master_text",
        "hashtags",
    )
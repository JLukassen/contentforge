from django.contrib import admin

from .models import SocialPost


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "telegram_status",
        "reddit_status",
        "x_status",
        "instagram_status",
        "created_at",
        "scheduled_for",
    )
    list_filter = (
        "status",
        "telegram_status",
        "reddit_status",
        "x_status",
        "instagram_status",
        "created_at",
        "scheduled_for",
    )
    search_fields = (
        "title",
        "master_text",
        "hashtags",
        "telegram_text",
        "telegram_message_id",
    )
    readonly_fields = (
        "x_text",
        "reddit_title",
        "reddit_body",
        "instagram_caption",
        "telegram_text",
        "telegram_message_id",
        "telegram_chat_id",
        "last_publish_error",
        "published_at",
    )

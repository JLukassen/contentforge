from django.contrib import admin

from .models import SocialPost


@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "scheduled_for")
    list_filter = ("status", "created_at", "scheduled_for")
    search_fields = ("title", "master_text", "hashtags")

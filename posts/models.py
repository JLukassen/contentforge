from django.db import models

from .services.formatter import (
    format_for_x,
    format_for_reddit,
    format_for_instagram,
)

from .services.hashtag_tools import normalize_hashtags


class SocialPost(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("ready", "Ready"),
        ("posted", "Posted"),
        ("archived", "Archived"),
    ]

    title = models.CharField(max_length=200)
    master_text = models.TextField()

    x_text = models.TextField(blank=True)
    reddit_title = models.CharField(max_length=300, blank=True)
    reddit_body = models.TextField(blank=True)
    instagram_caption = models.TextField(blank=True)
    hashtags = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_for = models.DateTimeField(null=True, blank=True)

    def generate_platform_drafts(self):
        clean_hashtags = normalize_hashtags(self.hashtags)
        self.hashtags = clean_hashtags

        self.x_text = format_for_x(self.master_text)

        self.reddit_title, self.reddit_body = format_for_reddit(
            self.title,
            self.master_text,
        )

        self.instagram_caption = format_for_instagram(
            self.master_text,
            clean_hashtags,
        )

    def save(self, *args, **kwargs):
        self.generate_platform_drafts()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

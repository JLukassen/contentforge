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

    CATEGORY_CHOICES = [
        ("general", "General"),
        ("white_label", "White Label"),
        ("kpopalypse", "KpopalypseNow"),
        ("toolbox", "ToolBox"),
        ("personal_brand", "Personal Brand"),
        ("meme_caption", "Meme / Edit Caption"),
    ]

    PLATFORM_STATUS_CHOICES = [
        ("not_ready", "Not Ready"),
        ("draft", "Draft"),
        ("ready", "Ready"),
        ("posted", "Posted"),
        ("skipped", "Skipped"),
    ]

    title = models.CharField(max_length=200)
    master_text = models.TextField()

    image = models.ImageField(
     upload_to="post_images/",
        blank=True,
        null=True,
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="general",
    )

    x_text = models.TextField(blank=True)
    reddit_title = models.CharField(max_length=300, blank=True)
    reddit_body = models.TextField(blank=True)
    instagram_caption = models.TextField(blank=True)
    hashtags = models.TextField(blank=True)

    x_status = models.CharField(
        max_length=20,
        choices=PLATFORM_STATUS_CHOICES,
        default="draft",
    )

    reddit_status = models.CharField(
        max_length=20,
        choices=PLATFORM_STATUS_CHOICES,
        default="draft",
    )

    instagram_status = models.CharField(
        max_length=20,
        choices=PLATFORM_STATUS_CHOICES,
        default="draft",
    )

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
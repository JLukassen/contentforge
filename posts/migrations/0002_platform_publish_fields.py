# Generated manually for ContentForge platform publishing fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="socialpost",
            name="telegram_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="telegram_status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("ready", "Ready"),
                    ("posted", "Posted"),
                    ("failed", "Failed"),
                ],
                default="draft",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="reddit_status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("ready", "Ready"),
                    ("posted", "Posted"),
                    ("failed", "Failed"),
                ],
                default="draft",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="x_status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("ready", "Ready"),
                    ("posted", "Posted"),
                    ("failed", "Failed"),
                ],
                default="draft",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="instagram_status",
            field=models.CharField(
                choices=[
                    ("draft", "Draft"),
                    ("ready", "Ready"),
                    ("posted", "Posted"),
                    ("failed", "Failed"),
                ],
                default="draft",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="telegram_chat_id",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="telegram_message_id",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="reddit_post_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="x_post_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="instagram_post_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="last_publish_error",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="socialpost",
            name="published_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

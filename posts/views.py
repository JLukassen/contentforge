from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SocialPostForm
from .models import SocialPost
from .services.telegram import TelegramPublishError, publish_to_telegram


def post_list(request):
    selected_status = request.GET.get("status", "")
    search_query = request.GET.get("q", "").strip()

    posts = SocialPost.objects.order_by("-created_at")

    if selected_status:
        posts = posts.filter(status=selected_status)

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    status_counts = SocialPost.objects.values("status").annotate(total=Count("id"))
    status_summary = {item["status"]: item["total"] for item in status_counts}
    status_cards = [
        {
            "value": value,
            "label": label,
            "total": status_summary.get(value, 0),
        }
        for value, label in SocialPost.STATUS_CHOICES
    ]

    context = {
        "posts": posts,
        "selected_status": selected_status,
        "search_query": search_query,
        "status_choices": SocialPost.STATUS_CHOICES,
        "status_cards": status_cards,
        "total_posts": SocialPost.objects.count(),
    }
    return render(request, "posts/post_list.html", context)


def post_create(request):
    if request.method == "POST":
        form = SocialPostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = SocialPostForm()

    return render(request, "posts/post_create.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def post_preview(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)
    return render(request, "posts/post_preview.html", {"post": post})


def post_update(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)

    if request.method == "POST":
        form = SocialPostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = SocialPostForm(instance=post)

    return render(request, "posts/post_create.html", {"form": form, "post": post})


def post_publish_telegram(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)

    if request.method != "POST":
        return redirect("post_detail", pk=post.pk)

    try:
        result = publish_to_telegram(post.telegram_text)
    except TelegramPublishError as exc:
        post.telegram_status = "failed"
        post.last_publish_error = str(exc)
        post.save(update_fields=["telegram_status", "last_publish_error", "updated_at"])
        return redirect("post_detail", pk=post.pk)

    post.telegram_status = "posted"
    post.telegram_message_id = result["message_id"]
    post.telegram_chat_id = result["chat_id"]
    post.last_publish_error = ""
    post.published_at = timezone.now()
    post.save(
        update_fields=[
            "telegram_status",
            "telegram_message_id",
            "telegram_chat_id",
            "last_publish_error",
            "published_at",
            "updated_at",
        ]
    )
    return redirect("post_detail", pk=post.pk)


def post_delete(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return redirect("post_detail", pk=post.pk)

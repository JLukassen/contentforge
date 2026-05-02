from django.shortcuts import render, redirect, get_object_or_404

from .forms import SocialPostForm
from .models import SocialPost


def post_list(request):
    category = request.GET.get("category")
    status = request.GET.get("status")

    posts = SocialPost.objects.order_by("-created_at")

    if category:
        posts = posts.filter(category=category)

    if status:
        posts = posts.filter(status=status)

    context = {
        "posts": posts,
        "category_choices": SocialPost.CATEGORY_CHOICES,
        "status_choices": SocialPost.STATUS_CHOICES,
        "selected_category": category,
        "selected_status": status,
    }

    return render(request, "posts/post_list.html", context)


def post_create(request):
    if request.method == "POST":
        form = SocialPostForm(request.POST, request.FILES)

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
        form = SocialPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = SocialPostForm(instance=post)

    return render(request, "posts/post_create.html", {"form": form, "post": post})


def post_archive(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)
    post.status = "archived"
    post.save()
    return redirect("post_list")


def post_delete(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "posts/post_confirm_delete.html", {"post": post})
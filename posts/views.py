from django.shortcuts import render, redirect, get_object_or_404

from .forms import SocialPostForm
from .models import SocialPost


def post_list(request):
    posts = SocialPost.objects.order_by("-created_at")
    return render(request, "posts/post_list.html", {"posts": posts})


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
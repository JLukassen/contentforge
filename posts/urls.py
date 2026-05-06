from django.urls import path

from . import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("new/", views.post_create, name="post_create"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>/preview/", views.post_preview, name="post_preview"),
    path("<int:pk>/edit/", views.post_update, name="post_update"),
    path("<int:pk>/publish/telegram/", views.post_publish_telegram, name="post_publish_telegram"),
    path("<int:pk>/delete/", views.post_delete, name="post_delete"),
]

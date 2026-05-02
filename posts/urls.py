from django.urls import path

from . import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("new/", views.post_create, name="post_create"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:pk>/preview/", views.post_preview, name="post_preview"),
]

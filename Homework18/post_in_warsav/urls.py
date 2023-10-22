from django.urls import path, include
from .views import post_view, PostListView

urlpatterns = [
    path("all_posts_func/", post_view, name="all_posts_func"),
    path("all_posts_class/", PostListView.as_view(), name="all_posts_class"),
]
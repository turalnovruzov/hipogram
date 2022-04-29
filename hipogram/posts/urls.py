from django.urls import path

from hipogram.posts.views import post_list_view, CreatePostView

app_name = "posts"

urlpatterns = [
    path("", post_list_view, name="list"),
    path("create_post", CreatePostView.as_view(), name="create")
]

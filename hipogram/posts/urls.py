from django.urls import path

from hipogram.posts.views import post_list_view, ListPostsView, CreatePostView

app_name = "posts"

urlpatterns = [
    path("", ListPostsView.as_view(), name="list"),
    path("create_post", CreatePostView.as_view(), name="create")
]

from django.urls import path

from hipogram.posts.views import ListPostsView, CreatePostView, UpdatePostView, DeletePostView

app_name = "posts"

urlpatterns = [
    path("", ListPostsView.as_view(), name="list"),
    path("posts/create", CreatePostView.as_view(), name="create"),
    path("posts/<int:pk>/update", UpdatePostView.as_view(), name="update"),
    path("posts/<int:pk>/delete", DeletePostView.as_view(), name="delete")
]

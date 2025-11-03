from django.urls import path
from .views import PostListCreateAPIView

urlpatterns = [
    path("api/posts/", PostListCreateAPIView.as_view(), name="post-list-create"),
]

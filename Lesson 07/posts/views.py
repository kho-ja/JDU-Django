from django.shortcuts import get_object_or_404, render
from .models import Post


def index(request):
    return render(
        request, "posts/index.html", {"posts": Post.objects.order_by("-created_at")}
    )


def detail(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detail.html", {"post": post})

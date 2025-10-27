from django.contrib import admin
from django.urls import include, path
import books.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("books/", include("books.urls")),
    path("posts/", include("posts.urls")),
    path("redirect_me/<int:book_id>/", books.views.redirect_me),
]

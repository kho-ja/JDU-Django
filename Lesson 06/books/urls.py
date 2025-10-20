from . import views
from django.urls import path

app_name = "books"

urlpatterns = [
    path('', views.books, name='all'),
    path('<int:book_id>/', views.book_detail, name='one'),
]

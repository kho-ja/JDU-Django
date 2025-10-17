from django.urls import path
from .views import index, view

urlpatterns = [
    path('', index, name='index'),
    path('<int:student_id>', view, name='view'),
]

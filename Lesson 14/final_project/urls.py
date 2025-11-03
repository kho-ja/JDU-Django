"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import login_page, register_page, logout_view, profile_page
from students.views import students_page

urlpatterns = [
    path("admin/", admin.site.urls),
    # Authentication URLs
    path("", login_page, name="login"),
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
    path("logout/", logout_view, name="logout"),
    # Profile URLs
    path("profile/", profile_page, name="profile"),
    # Students URLs
    path("students/", students_page, name="students"),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 handler
handler404 = "profiles.views.custom_404"

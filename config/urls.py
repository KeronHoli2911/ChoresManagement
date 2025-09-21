"""
URL configuration for config project.

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
from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    # Family
    path("families/", views.FamilyListView.as_view(), name="family_list"),
    path("families/create/", views.FamilyCreateView.as_view(), name="family_create"),
    path("families/<int:pk>/", views.FamilyDetailView.as_view(), name="family_detail"),
    path("families/<int:pk>/update/", views.FamilyUpdateView.as_view(), name="family_update"),
    path("families/<int:pk>/delete/", views.FamilyDeleteView.as_view(), name="family_delete"),

    # Login / Logout
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
] 
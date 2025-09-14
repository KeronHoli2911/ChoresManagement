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
from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("create/", views.TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    
    path("categories/", TaskCategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>/", TaskCategoryDetailView.as_view(), name="category_detail"),
    path("categories/create/", TaskCategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/update/", TaskCategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", TaskCategoryDeleteView.as_view(), name="category_delete"),
]

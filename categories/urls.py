from django.urls import path
from .views import (
    TaskCategoryListView,
    TaskCategoryCreateView,
    TaskCategoryDetailView,
    TaskCategoryUpdateView,
    TaskCategoryDeleteView,
)

app_name = 'tasks'

urlpatterns = [
    path("categories/", TaskCategoryListView.as_view(), name="category_list"),
    path("categories/create/", TaskCategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/", TaskCategoryDetailView.as_view(), name="category_detail"),
    path("categories/<int:pk>/update/", TaskCategoryUpdateView.as_view(), name="category_update"),
    path("categories/<int:pk>/delete/", TaskCategoryDeleteView.as_view(), name="category_delete"),
]
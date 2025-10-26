from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TaskCategory
from .forms import TaskCategoryForm


class TaskCategoryListView(ListView):
    model = TaskCategory
    template_name = 'tasks/taskcategory_list.html'
    context_object_name = 'categories'


class TaskCategoryDetailView(DetailView):
    model = TaskCategory
    template_name = 'tasks/taskcategory_detail.html'
    context_object_name = 'category'


class TaskCategoryCreateView(CreateView):
    model = TaskCategory
    form_class = TaskCategoryForm
    template_name = 'tasks/taskcategory_form.html'
    success_url = reverse_lazy('tasks:category_list')


class TaskCategoryUpdateView(UpdateView):
    model = TaskCategory
    form_class = TaskCategoryForm
    template_name = 'tasks/taskcategory_form.html'
    success_url = reverse_lazy('tasks:category_list')


class TaskCategoryDeleteView(DeleteView):
    model = TaskCategory
    template_name = 'tasks/taskcategory_confirm_delete.html'
    success_url = reverse_lazy('tasks:category_list')
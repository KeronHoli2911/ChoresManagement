from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Family
from .forms import FamilyForm, CustomLoginForm
# Create your views here.

class FamilyListView(LoginRequiredMixin, ListView):
    model = Family
    template_name = "accounts/family_list.html"
    context_object_name = "families"


class FamilyDetailView(LoginRequiredMixin, DetailView):
    model = Family
    template_name = "accounts/family_detail.html"
    context_object_name = "family"


class FamilyCreateView(LoginRequiredMixin, CreateView):
    model = Family
    form_class = FamilyForm
    template_name = "accounts/family_form.html"
    success_url = reverse_lazy("accounts:family_list")


class FamilyUpdateView(LoginRequiredMixin, UpdateView):
    model = Family
    form_class = FamilyForm
    template_name = "accounts/family_form.html"
    success_url = reverse_lazy("accounts:family_list")


class FamilyDeleteView(LoginRequiredMixin, DeleteView):
    model = Family
    template_name = "accounts/family_confirm_delete.html"
    success_url = reverse_lazy("accounts:family_list")

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy("accounts:family_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Вхід"
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return reverse_lazy("home")  
        return super().dispatch(request, *args, **kwargs)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")
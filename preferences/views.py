from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import UserPreferences
from .forms import UserPreferencesForm
# Create your views here.

class UserPreferencesUpdateView(LoginRequiredMixin, UpdateView):
    model = UserPreferences
    form_class = UserPreferencesForm
    template_name = "preferences/preferences_form.html"
    success_url = reverse_lazy("preferences_view")

    def get_object(self, queryset=None):
        obj, created = UserPreferences.objects.get_or_create(user=self.request.user)
        return obj
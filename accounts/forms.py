from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Family


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ["name", "description"]
        labels = {
            "name": "Назва сім'ї",
            "description": "Опис",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
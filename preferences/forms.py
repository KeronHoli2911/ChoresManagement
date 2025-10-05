from django import forms
from .models import UserPreferences

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ["liked_categories", "disliked_categories", "availability", "experience_levels", "physical_limitations"]

        widgets = {
            "liked_categories": forms.CheckboxSelectMultiple(),
            "disliked_categories": forms.CheckboxSelectMultiple(),
            "availability": forms.Textarea(attrs={"class": "form-control"}),
            "experience_levels": forms.Textarea(attrs={"class": "form-control"}),
            "physical_limitations": forms.Textarea(attrs={"class": "form-control"}),
        }

        help_texts = {
            "availability": "Введіть у форматі JSON. Напр.: {'monday': ['09:00-12:00']}",
            "experience_levels": "Введіть у форматі JSON. Напр.: {'cooking': 3}",
        }
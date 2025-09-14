from django import forms
from .models import Task
from .models import TaskCategory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date', 'progress']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва завдання'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис завдання', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'progress': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }


class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = ["name", "description", "color", "is_active"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control","placeholder": "Введіть назву категорії",}),
            "description": forms.Textarea(attrs={"class": "form-control","placeholder": "Додайте опис (необов'язково)","rows": 3,}),
            "color": forms.TextInput(attrs={"type": "color",}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input",}),
        }
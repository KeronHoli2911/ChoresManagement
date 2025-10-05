from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    liked_categories = models.ManyToManyField(Category, blank=True, related_name="liked_by")
    disliked_categories = models.ManyToManyField(Category, blank=True, related_name="disliked_by")
    availability = models.JSONField(default=dict, blank=True)
    experience_levels = models.JSONField(default=dict, blank=True)
    physical_limitations = models.TextField(blank=True)

    class Meta:
        verbose_name = "Налаштування користувача"
        verbose_name_plural = "Налаштування користувачів"

    def __str__(self):
        return f"Налаштування користувача {self.user.username}"
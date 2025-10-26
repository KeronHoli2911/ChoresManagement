from django.db import models


class TaskCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Category Name"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Icon (CSS class or emoji)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task Category"
        verbose_name_plural = "Task Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
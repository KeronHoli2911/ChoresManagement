from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name


class User(AbstractUser):
    PARENT = "parent"
    CHILD = "child"

    ROLE_CHOICES = [
        (PARENT, "Батько/Мати"),
        (CHILD, "Дитина"),
    ]

    family = models.ForeignKey(
        Family,
        on_delete=models.SET_NULL,
        related_name="members",
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=CHILD
    )
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
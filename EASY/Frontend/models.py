from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from .forms import *

plans = [
    ('Starter', 'Starter'),
    ('Regular', 'Regular'),
    ('Advanced', 'Advanced'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # plan = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    plan = models.CharField(max_length=20, choices=plans, default='Starter')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name_plural = "Profiles"

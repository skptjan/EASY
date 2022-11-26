from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

PLANS = [
    ('Starter', 'Starter'),
    ('Regular', 'Regular'),
    ('Advanced', 'Advanced'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)
    # plan = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    plan = models.CharField(max_length=20, choices=PLANS, default='Starter')

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        verbose_name_plural = "Profiles"


class PlansForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['plan', 'user']


class Plan(models.Model):
    plan_name = models.CharField(max_length=20, choices=PLANS, default='Starter', unique=True)
    plan_price = models.FloatField(default=0)
    number_off_areas = models.IntegerField(default=0)
    number_off_lamps = models.IntegerField(default=0)
    number_off_functions = models.IntegerField(default=0)
    plan_description = models.TextField(default=0)

    def __str__(self):
        return f"{self.plan_name}"

    class Meta:
        verbose_name_plural = "Plans"

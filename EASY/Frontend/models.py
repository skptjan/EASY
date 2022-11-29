from django.db import models, transaction
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

PLANS = [
    ('Starter', 'Starter'),
    ('Regular', 'Regular'),
    ('Advanced', 'Advanced'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)
    plan = models.CharField(max_length=20, choices=PLANS, default='Starter')


    # @transaction.atomic
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance, plan=sender.plan)
    #         instance.profile.save()
    #
    # @transaction.atomic
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    def __str__(self):
        return f"{self.user.username}'s profile, {self.plan}"
    class Meta:
        verbose_name_plural = "Profiles"


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

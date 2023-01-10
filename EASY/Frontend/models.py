import time

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
        return f"{self.user.username}'s profile, userid: {self.user.id}, id: {self.id}, {self.plan}"
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


class contact(models.Model):
    name = models.CharField(max_length=200, default=" ")
    email = models.EmailField(max_length=200, default=" ")
    bericht = models.TextField(max_length=200, default=" ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"


class Lamp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, default=User)
    lamp_name = models.CharField(max_length=200, default="Lamp name")
    time_set_on = models.TimeField(auto_now=False, auto_now_add=False, default="00:00:00")
    time_set_off = models.TimeField(auto_now=False, auto_now_add=False, default="00:00:00")
    # datetime_set_on = models.DateTimeField(auto_now=False, auto_now_add=False, default="2020-01-01 00:00:00")
    # datetime_set_off = models.DateTimeField(auto_now=False, auto_now_add=False, default="2020-01-01 00:00:00")

    def __str__(self):
        return self.lamp_name

    class Meta:
        verbose_name_plural = "User Lamps"

class LampLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    on = models.BooleanField()

    def __str__(self):
        notNone = self.time
        date = None
        if notNone:
            date = notNone.strftime("%d/%m/%Y, %H:%M:%S")
        return ("id: %s, user: %s, DateTime: %s, IsOn: %s" % (self.id, self.user, date if notNone else "", self.on))

    class Meta:
        verbose_name_plural = "Lamp Log"
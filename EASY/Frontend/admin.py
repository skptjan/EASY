from django.contrib import admin
from .models import Plan, Profile, contact, Lamp

# Register your models here.
admin.site.register(Lamp)
admin.site.register(contact)
admin.site.register(Plan)
admin.site.register(Profile)



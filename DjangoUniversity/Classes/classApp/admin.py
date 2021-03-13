from django.contrib import admin
from .models import djangoClasses

# Registering model here.  Must import the classes from the models module.
admin.site.register(djangoClasses)

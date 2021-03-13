from django.db import models


# This creates a dB table in the project's database.
class djangoClasses(models.Model):
    # Define attributes (columns) in dB. Can add a 'choices' attribute to create pulldown menu of options.
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField(max_length=10)
    instructor = models.CharField(max_length=60)
    duration = models.FloatField(max_length=20)

    # Object manager for managing objects of this class.
    objects = models.Manager()



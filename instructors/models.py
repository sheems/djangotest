from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    course = models.CharField(max_length=64)

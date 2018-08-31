from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(verbose_name='Instructor Name', max_length=255, help_text="This is name")
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    course = models.CharField(max_length=255)
    slug = model.Slugsfield(unique=True)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, choices=('m', 'Male'), ('f', 'Female'))

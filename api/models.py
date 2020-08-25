from django.db import models


# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=70, blank=False, default='', primary_key=True)
    password = models.CharField(max_length=200, blank=False, default='')
    phonenumber = models.CharField(max_length=200, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')

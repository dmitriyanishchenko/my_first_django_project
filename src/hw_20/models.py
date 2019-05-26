from django.db import models


class Car(models.Model):
   brand = models.CharField(max_length=255)
   model = models.CharField(max_length=255)
   color = models.CharField(max_length=255)
   weight = models.IntegerField()
   fullname = models.CharField(max_length=255)
   year = models.CharField(max_length=255)
# Create your models here.

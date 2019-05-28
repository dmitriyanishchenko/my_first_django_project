from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    weight = models.IntegerField()
    fullname = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

    def __str__(self):
        return f' {self.brand} {self.model} {self.color} {self.weight} {self.fullname} {self.year}'



# Create your models here.

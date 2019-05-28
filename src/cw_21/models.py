from django.db import models

class ContactInfo(models.Model):
   phone = models.CharField(max_length=50, null=True, default=None)
   address = models.CharField(max_length=50, null=True, default=None)

class Person(models.Model):
   firstname = models.CharField(max_length=255, default=None)
   lastname = models.CharField(max_length=255, default=None)
   age = models.IntegerField()
   profession = models.CharField(max_length=255, default=None)
   contact_info = models.OneToOneField(
       ContactInfo, null=True,
       related_name='person',
       on_delete=models.SET_NULL,
   )



# Create your models here.

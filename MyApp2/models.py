from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    mob_no=models.IntegerField()
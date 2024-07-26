from django.db import models

# Create your models here.
class Menu(models.Model):
    
    dish = models.CharField(max_length=200)
    price = models.IntegerField()
    cuisine = models.CharField(max_length=200)
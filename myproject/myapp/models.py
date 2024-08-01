from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact text")
    

class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField("Phone number",max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return f"{self.name}"
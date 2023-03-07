from django.db import models
from django import forms



# Create your models here.
class Dog(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    

    def __str__(self):
        return self.name
    

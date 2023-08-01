from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Car(models.Model):
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=500)
    price_day = models.IntegerField(max_length=10)
    price_week = models.IntegerField(max_length=10)
    price_month = models.IntegerField(max_length=10)
    image = models.ImageField(upload_to='appcar/images/')
    url = models.URLField(blank=True)

class Questions(models.Model):
    username = models.CharField(max_length=25)
    phone = PhoneNumberField(null=True, blank=True)
    question = models.CharField(max_length=500)
    
# Create your models here.

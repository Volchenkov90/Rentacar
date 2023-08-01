from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mark_condition = models.IntegerField(max_length=1)
    mark_staff = models.IntegerField(max_length=1)
    mark_cost = models.IntegerField(max_length=1)
    mark_location = models.IntegerField(max_length=1)
    average_mark = models.FloatField(max_length=3)
    
    def __str__(self):
        return self.text
# Create your models here.

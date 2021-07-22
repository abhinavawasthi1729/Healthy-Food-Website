from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122, default='abc')
    email=models.CharField(max_length=122, default='abc@gmail.com')
    phone= models.CharField(max_length=12, default='123')
    desc= models.TextField(default='no comments')
    date= models.DateField(default=datetime.today())
    
    def __str__(self):
        return self.name

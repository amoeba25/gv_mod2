from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    
    title = models.CharField(max_length=100, default= None)
    client = models.CharField(max_length=100, default= None)
    requested_by = models.CharField(max_length=100, default= None)
    type = models.CharField(max_length=100, default= None)
    description = models.CharField(max_length=200, default= None)
    assigned = models.ForeignKey(User, on_delete= models.CASCADE,to_field="username", blank= True, null= True)
    labels = models.CharField(max_length= 100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= 'New')
    
    
    def __str__(self):
        return self.title
    


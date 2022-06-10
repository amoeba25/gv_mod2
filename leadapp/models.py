from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Leads(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('Discussion', 'Discussion'),
        ('Negotiation', 'Negotiation'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    )
    
    company = models.CharField(max_length=100, default= None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= None)
    source = models.CharField(max_length=100,  default= None)
    owner = models.ForeignKey(User, on_delete= models.CASCADE,to_field="username")
    address = models.CharField(max_length=200, default= None)
    city = models.CharField(max_length=100, default= None)
    state = models.CharField(max_length=100, default= None)
    zip = models.CharField(max_length=100, default= None)
    country = models.CharField(max_length=100, default= None)
    phone = models.CharField(max_length=10, default= None)
    website = models.CharField(max_length= 150, default= None)
    vat = models.CharField(max_length=20, default= None)
    currency = models.CharField(max_length= 20, default= None)
    symbol = models.CharField(max_length=10,  default= None)
    
    
    def __str__(self):
        return self.company
    
class Contact(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    f_name = models.CharField(max_length=100, default= None)
    l_name = models.CharField(max_length=100, default= None)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default= None)
    skype = models.CharField(max_length=100, default= None)
    title = models.CharField(max_length= 50)
    gender = models.CharField(max_length=20 , choices= GENDER_CHOICES, default="None")
    
    def __str__(self):
        return self.f_name + "contact"
    
from django.db import models

# Create your models here.

# customer model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

# product model
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price =models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()


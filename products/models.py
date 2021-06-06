from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=230)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2300)
class Offer(models.Model):
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

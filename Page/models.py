from django.db import models


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=16)
    price = models.IntegerField()

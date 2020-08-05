from django.db import models


# Create your models here.
class Custom(models.Model):
    name = models.CharField(max_length=32)


class Goods(models.Model):
    name = models.CharField(max_length=32)
    custom = models.ManyToManyField(to=Custom)



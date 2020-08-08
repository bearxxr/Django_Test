from django.db import models


class Women(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()

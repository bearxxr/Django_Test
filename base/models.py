from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'


class Man(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'man'


class Woman(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    man = models.ForeignKey(Man,on_delete=models.CASCADE)

    class Meta:
        db_table = 'women'

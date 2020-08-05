from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    class Meta:
        db_table = 'person'


class Order(models.Model):
    o_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'


class Custom(models.Model):
    name = models.CharField(max_length=32)
    cost = models.IntegerField()

    class Meta:
        db_table = 'custom'


class Grade(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'm_grade'


class Student(models.Model):
    name = models.CharField(max_length=32)
    grade = ForeignKey(Grade, models.CASCADE)

    class Meta:
        db_table = 'm_student'


class Company(models.Model):
    name = models.CharField(max_length=32)
    girl_num = models.IntegerField()
    boy_num = models.IntegerField()

    class Meta:
        db_table = 'company'






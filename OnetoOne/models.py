from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=16)


class IdCard(models.Model):
    id_num = models.IntegerField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)

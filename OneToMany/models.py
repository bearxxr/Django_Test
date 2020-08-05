from django.db import models


# Create your models here.
# 部门表
class Dept(models.Model):
    name = models.CharField(max_length=32, verbose_name='名字')

    class Meta:
        db_table = 'dept'


class Emp(models.Model):
    name = models.CharField(max_length=32, verbose_name='名字')
    dept = models.ForeignKey(to=Dept, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table = 'emp'

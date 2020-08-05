from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from OneToMany.models import Dept, Emp


def adddept(request):
    dept = Dept()
    dept.name = '开发部'
    dept.save()

    return HttpResponse('添加成功')


def addemp(request):
    emp = Emp()
    emp.name = '袁隆平'
    emp.save()

    return HttpResponse('添加成功')


def bind(request):
    emp = Emp.objects.last()
    dept = Dept.objects.last()

    emp.dept = dept
    emp.save()

    return HttpResponse('绑定成功')


def deleteemp(request):
    emp = Emp.objects.last()
    emp.delete()

    return HttpResponse('删除成功')


def deletedept(request):
    dept = Dept.objects.last()
    dept.delete()

    return HttpResponse('删除成功')


def getemp(request):
    dept = Dept.objects.last()
    emps = dept.emp_set.all()
    for emp in emps:
        print(emp.id, emp.name)

    return HttpResponse('查询成功')


def getdept(request):

    emp = Emp.objects.last()
    dept = emp.dept
    print(dept.id, dept.name)

    return HttpResponse('查询成功')

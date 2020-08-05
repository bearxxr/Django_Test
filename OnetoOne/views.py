from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from OnetoOne.models import Student, IdCard


def addstudent(request):
    student = Student()
    student.name = '张三'
    student.save()
    return HttpResponse('添加成功')


def addidcard(request):
    idcard = IdCard()
    idcard.id_num = '123'

    # student = Student.objects.first()

    # idcard.student = student
    idcard.save()
    return HttpResponse('添加成功')


def bind(request):
    return HttpResponse('绑定成功')


def deleteidcard(request):
    idcard = IdCard.objects.last()
    idcard.delete()

    # 写这一步，我是shabi
    # idcard.save()

    return HttpResponse('删除成功')


def deleteCascade(request):
    student = Student.objects.last()
    student.delete()
    return HttpResponse('删除成功')


def getidcard(request):

    student = Student.objects.last()
    print(student.idcard.id_num)

    return HttpResponse('查询成功')


def getstudent(request):

    idcard = IdCard.objects.last()
    print(idcard.student.name)

    return HttpResponse('查询成功')

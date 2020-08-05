from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from base.models import Student, Man, Woman


def index(request):
    context = {
        'name': 'zs',
        'age': 18
    }
    return render(request, 'index.html', context=context)


def addstudent(request):
    student = Student()
    student.name = 'zs'
    student.age = 18
    student.save()
    return HttpResponse('添加成功')


def findstudent(request):
    student_list = Student.objects.all()
    for s in student_list:
        print(s.name, s.age)
    return HttpResponse('添加成功')


def updatestudent(request):
    student = Student.objects.get(id=1)
    student.name = '早上'
    student.save()
    return HttpResponse('修改成功')


def deletestudent(request):
    student = Student.objects.get(name='早上')
    student.delete()
    return HttpResponse('删除成功')


# 查询数据
def man_get_woman(request):
    man = Man.objects.get(id=1)
    women_list = man.woman_set.all()
    for women in women_list:
        print(women.name, women.age)
    return HttpResponse('查询成功')


def woman_get_man(request):
    woman = Woman.objects.get(id=1)
    man = woman.man
    print(man.name, man.id)
    return HttpResponse('查询成功')

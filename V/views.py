from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse('test')


def testRoute(request, id):
    return HttpResponse('测试成功')


def testLocals(request):
    name = 'zs'
    age = 18
    return render(request, 'testLocals.html', context=locals())


def index(request):
    return render(request, 'index.html')


def testReverse(request):
    return HttpResponse('Django方向解析吃；成功')


def testPosition(request,year,day,month):
    return HttpResponse(year+'/'+month+'/'+day)

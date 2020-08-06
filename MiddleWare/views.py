import random

from django.http import HttpResponse
from django.shortcuts import render


def find(request):
    print('链接数据库')
    return HttpResponse('find')


def add(request):
    print('链接数据库')
    return HttpResponse('add')


def delete(request):
    print('链接数据库')
    return HttpResponse('delete')


def update(request):
    print('链接数据库')
    return HttpResponse('update')


def getphone(request):
    result = random.randrange(100)
    if result > 80:
        print(result)
        return HttpResponse('恭喜你抢到了')
    else:
        return HttpResponse('没货了')


def testexception(request):

    a = 1
    b = 2
    c = 0
    d = a/c

    return HttpResponse('现在没有报错哦')

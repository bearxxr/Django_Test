from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ManyToMany.models import Custom, Goods


def addcustom(request):
    custom = Custom()
    custom.name = '超市商品'
    custom.save()

    return HttpResponse('添加成功')


def addgoods(request):
    goods = Goods()
    goods.name = '营养快线'
    goods.save()

    return HttpResponse('添加成功')


def bind(request):
    custom = Custom.objects.last()
    goods = Goods.objects.last()
    custom.goods_set.add(goods)

    return HttpResponse('绑定成功')


def bind2(request):
    custom = Custom.objects.last()
    goods = Goods.objects.last()
    goods.custom.add(custom)

    return HttpResponse('绑定成功')


def deleterelation(request):
    custom = Custom.objects.last()
    goods = Goods.objects.last()
    custom.goods_set.remove(goods)

    return HttpResponse('删除成功')


def deleterelation2(request):
    custom = Custom.objects.last()
    goods = Goods.objects.last()

    goods.custom.remove(custom)

    return HttpResponse('删除成功')


def deletecustom(request):
    custom = Custom.objects.last()
    custom.delete()

    return HttpResponse('删除成功')


def deletegoods(request):
    goods = Goods.objects.last()
    goods.delete()

    return HttpResponse('删除成功')


def selectgoods(request):
    custom = Custom.objects.last()
    goods = custom.goods_set.all()
    for good in goods:
        print(good.name)

    return HttpResponse('查询成功')


def selectcustom(request):
    goods = Goods.objects.last()
    custom_list = goods.custom.all()
    print(type(custom_list))
    for custom in custom_list:
        print(custom.id,custom.name)


    return HttpResponse('查询成功')

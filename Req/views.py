from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_control


def test(request):
    return HttpResponse('测试成功')


@cache_control(timeout=300)
def testRequest(request):
    # 请求资源路径
    print(request.path)
    # 请求方法
    print(request.method)
    # 请求
    print(type(request.GET))
    print(type(request.POST))

    print(request.GET.get('name'))

    return HttpResponse('测试成功')

import time

from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(20)
def testcache(request):
    time.sleep(7)

    return HttpResponse('这是缓存哦')


def datachche(request):
    print(request.META.get('REMOTE_ADDR'))
    ip = cache.get('ip')
    if ip:
        return HttpResponse('已经向缓存表中写入数据')
    else:
        cache.set('ip', request.META.get('REMOTE_ADDR'))
        return HttpResponse('测试缓存哦')


def redischche(request):
    ip = cache.get('ip')
    if ip:
        return HttpResponse('测试缓存哦！！！')
    else:
        value = request.META.get('REMOTE_ADDR')
        print(value)
        cache.set('ip', value)

        return HttpResponse('向redis写入中')

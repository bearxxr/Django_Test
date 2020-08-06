import random

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class ConnctionMiddle(MiddlewareMixin):

    def process_request(self, request):
        # print('这是请求之前的中间件')
        result = random.randrange(100)
        if result > 60:
            print(result)
            # return HttpResponse('你利用特权抢到了！！！')


class ExceptionAop(MiddlewareMixin):

    def process_exception(self, request, exception):
        return HttpResponse('我已经捕获了错误哦')

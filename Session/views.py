from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView


class SessionLoginView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'sessionlogin.html')

    def post(self, request):
        name = request.POST.get('name')

        response = redirect(reverse('Sess:welcomesession'))

        request.session['name'] = name

        return response


class WelcomesessionView(ListView):

    def get(self, request, *args, **kwargs):
        name = request.session.get('name', '游客')

        return render(request, 'welcomesession.html', context=locals())


class SessionLoginoutView(ListView):
    def get(self, request, *args, **kwargs):

        # 删除session的方法
        # del request.session['name']

        response = redirect(reverse('Sess:welcomesession'))
        # response.delete_cookie('sessionid')

        # 全部删除
        request.session.flush()

        return response

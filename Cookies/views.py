from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView


class LoginView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request):
        name = request.POST.get('name', '游客')

        response = redirect(reverse('Cook:index'))
        response.set_cookie('name', name)

        return response


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        name = request.COOKIES.get('name', '游客')
        print(request.COOKIES)
        return render(request, 'indexCook.html', context=locals())

    # def post(self,request):
    #
    #     response = redirect(reverse('Cook:index'))
    #
    #     response.delete_cookie('name')
    #
    #     return render(request,'indexCook.html')


class LoginOutView(ListView):
    def get(self, request, *args, **kwargs):
        response = redirect(reverse('Cook:index'))
        response.delete_cookie('name')
        return response


def loginout(request):
    response = redirect(reverse('Cook:index'))
    response.delete_cookie('name')
    return response


def setsaltcookie(request):
    response = redirect(reverse('Cook:setsaltcookie1'))
    response.set_signed_cookie('name', 'zs',salt='x')

    return response


def setsaltcookie1(request):

    name = request.get_signed_cookie('name',salt='x')
    print(name)

    return HttpResponse(name)

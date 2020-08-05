from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Res.models import Animal


def test(request):
    response = HttpResponse()
    response.content = '123321'

    return response


def testRedirect(request):
    responsered = HttpResponseRedirect('/')
    print(isinstance(responsered, HttpResponse))
    print(type(responsered))
    return HttpResponseRedirect('/Res/test/')


def testArgs(request):
    return redirect(reverse('Res:Args', args=[2020, 8, 1]))
    # print((reverse('Res:Args')))
    # return HttpResponse('测试成功')


def Args1(request, month, day, year):
    return HttpResponse(year + '/' + month + '/' + day)


def testKargs(request):
    return redirect(reverse('Res:Kargs', kwargs={'year': 2020, 'month': 8, 'day': 1}))


def Kargs(request, month, day, year):
    return HttpResponse(year + '/' + month + '/' + day)


def testResObj(request):
    animal = Animal.objects.first()
    data = {
        'animal': animal.to_dict
    }
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


def testResList(request):

    animals = Animal.objects.all()
    animal_list = []
    for animal in animals:
        animal_list.append(animal.to_dict)

    data = {
        'animals': animal_list
    }

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})

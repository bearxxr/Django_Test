from django.shortcuts import render

# Create your views here.
from T.models import Dog


def test(request):
    context = {
        "name": '老王'
    }
    return render(request, 'test.html', context=context)


def testPoint(request):
    dog = Dog.objects.first()

    context = {
        'dog': dog
    }

    return render(request, 'testPoint.html', context=context)


def testTag(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs,
        'num': 5,
        'code': 'abcd'
    }
    return render(request, 'testTag.html', context=context)


def getStatic(request):
    return render(request, 'getStatic.html')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Final.models import User


def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':

        icon = request.FILES.get('icon')
        print(type(icon))
        print(icon)

        with open('/home/bear/桌面/Django_model/static/icon.jpg', 'wb') as f:
            for content in icon.chunks():
                f.write(content)
                f.flush()

        return HttpResponse('上传成功')


def uploadDjango(request):

    if request.method == 'GET':
        return render(request, 'uploadDjango.html')
    if request.method == 'POST':
        icon = request.FILES.get('icon')
        print(icon)

        user = User()
        user.icon = icon
        user.save()

        return HttpResponse('上传成功')

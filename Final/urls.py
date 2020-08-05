from django.conf.urls import url
from django.urls import re_path, path

from Final import views

urlpatterns = [
    # 自己上传文件
    re_path(r'^upload/$', views.upload, name='upload'),
    # 利用Django上传
    url(r'^uploadDjango/$', views.uploadDjango, name='uploadDjango'),
]

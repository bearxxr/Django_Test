from django.conf.urls import url
from django.conf.urls import re_path

from V import views

urlpatterns = [
    url(r'test/',views.test),
    url(r'testRoute/(?P<id>\d+)/$',views.testRoute),

    url(r'testLocals/',views.testLocals),

    # 反向解析
    url(r'index/',views.index),
    # url(r'testReverse/',views.testReverse,name='testReverse'),
    re_path(r'testReverse/',views.testReverse,name='testReverse'),

    # 反向解析关键字字数
    re_path(r'testPosition/(?P<year>\d{4})/(?P<month>\d)/(?P<day>\d)$',views.testPosition,name='testPosition'),
]
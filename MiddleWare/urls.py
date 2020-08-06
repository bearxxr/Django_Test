from django.urls import re_path

from MiddleWare import views

urlpatterns = [
    re_path(r'^add/',views.add),
    re_path(r'^delete/',views.delete),
    re_path(r'^update/',views.update),
    re_path(r'^find/',views.find),

    # 黑白名单
    re_path(r'^getphone/',views.getphone),
    # 报错中间件
    re_path(r'^testexception/',views.testexception)
]
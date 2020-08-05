from django.urls import re_path

from Cache import views

urlpatterns = [
    re_path(r"^testcache/",views.testcache),
    # 测试数据库缓存
    re_path(r'^datacache/',views.datachche),
    # 测试redis缓存
    re_path(r'^rediscache/',views.redischche),
]
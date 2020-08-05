from django.urls import re_path
from django.conf.urls import url
from OnetoOne import views

urlpatterns = [
    # 主表添加数据
    re_path(r'^addstudent/', views.addstudent),
    # 从表添加数据
    re_path(r'^addidcard/', views.addidcard),
    # 数据绑定
    re_path(r'^bind/', views.bind),

    # 删除从表数据
    re_path(r'^deleteidcard/',views.deleteidcard),

    # 删除主表数据
    re_path(r'^deleteCascade/',views.deleteCascade),

    # 主表查询数据
    re_path(r'getidcard/',views.getidcard),
    # 从表查询主表数据
    re_path(r'getstudent/', views.getstudent),

]

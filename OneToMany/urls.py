from django.urls import re_path

from OneToMany import views

urlpatterns = [
    # 添加数据
    re_path(r'^adddept/',views.adddept),
    re_path(r'^addemp/',views.addemp),
    # 绑定外键
    re_path(r'^bind/',views.bind),

    # 删除从表数据
    re_path(r'^deleteemp/',views.deleteemp),
    # 删除从表数据
    re_path(r'^deletedept/',views.deletedept),

    # 主表查询从表
    re_path(r'^getemp/',views.getemp),
    # 从表查询主表
    re_path(r'^getdept/',views.getdept)
]
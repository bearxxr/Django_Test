from django.urls import re_path

from ManyToMany import views

urlpatterns = [
    # 添加数据
    re_path(r'^addcustom/',views.addcustom),
    re_path(r'^addgoods/',views.addgoods),
    # 添加第三张表
    re_path(r'^bind/',views.bind),
    re_path(r'^bind2/',views.bind2),

    # 删除关系表数据
    re_path(r'^deleterelation/',views.deleterelation),
    re_path(r'^deleterelation2/',views.deleterelation2),

    # 删除数据
    re_path(r'deletecustom/',views.deletecustom),
    re_path(r'deletegoods/',views.deletegoods),

    # 查询数据
    re_path(r'^selectgoods/',views.selectgoods),
    re_path(r'^selectcustom/',views.selectcustom),
]
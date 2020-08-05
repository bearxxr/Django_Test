from django.conf.urls import url

from base import views



urlpatterns = [
    url(r'^index/',views.index),

    url(r'addstudent',views.addstudent),
    url(r'findstudent',views.findstudent),
    url(r'updatestudent',views.updatestudent),
    url(r'deletestudent',views.deletestudent),

    # 外键关系
    url(r'man_get_woman',views.man_get_woman),
    url(r'woman_get_man',views.woman_get_man),

]
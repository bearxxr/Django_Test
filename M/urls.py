from django.conf.urls import url
from M import views

urlpatterns = [
    url(r'test/',views.test),
    url(r'getone/',views.getone),

    url(r'addorder/',views.addorder),
    url(r'getyear/',views.getyear),
    url(r'getmonth/',views.getmonth),


    url(r'getaggr/',views.getaggr),

    # 跨关系查询
    url(r'getstudents/',views.getstudents),

    # F,Q对象
    url(r'testF/',views.testF),
    url(r'testQ/',views.testQ),
]
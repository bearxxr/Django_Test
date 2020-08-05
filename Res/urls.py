from django.conf.urls import url


from Res import views

urlpatterns = [
    url(r'^test/',views.test),
    url(r'^testRedirect/',views.testRedirect),

    url(r'^testArgs/',views.testArgs),
    url(r'^Args/(\d+)/(\d+)/(\d+)',views.Args1,name='Args'),

    # 测试关键字参数
    url(r'^testKargs/',views.testKargs),
    url(r'^Kargs/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',views.Kargs,name='Kargs'),

    # 返回一个对象
    url(r'^testResObj/',views.testResObj),
    # 返回一个列表
    url(r'^testResList/',views.testResList),
]
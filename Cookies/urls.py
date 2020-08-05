from django.conf.urls import url

from Cookies import views
from Cookies.views import LoginView,IndexView,LoginOutView

urlpatterns = [
    url(r'^login/',LoginView.as_view(),name='login'),
    url(r'index/',IndexView.as_view(),name='index'),
    url(r'viewloginout/',LoginOutView.as_view(),name='viewloginout'),

    url(r'^loginout/',views.loginout,name='loginout'),

    # COOKIE加盐
    url(r'^setsaltcookie/',views.setsaltcookie,name='setsaltcookie'),
    url(r'^setsaltcookie1/',views.setsaltcookie1,name='setsaltcookie1'),
]
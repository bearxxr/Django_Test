"""Django_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from DRF import views

# 基础djangorestreframework
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^base/', include('base.urls')),

    url(r'M/', include('M.urls')),
    url(r'T/', include('T.urls')),
    url(r'V/', include(('V.urls', 'V'))),

    url(r'Req/', include('Req.urls')),
    url(r'Res/', include(('Res.urls', 'Res'))),
    url(r'^Cook/', include(('Cookies.urls', 'Cook'))),
    url(r'^Sess/', include(('Session.urls', 'Sess'))),
    url(r'^DB/', include(('DBmigrate.urls', 'DB'))),
    url(r'^One/', include(('OnetoOne.urls', 'One'))),
    url(r'^OnetoMany/', include(('OneToMany.urls', 'OnetoMany'))),
    url(r'^Many/', include(('ManyToMany.urls', 'Many'))),
    url(r'^Final/', include(('Final.urls', 'Final'))),
    url(r'^Cache/', include(('Cache.urls', 'Cache'))),
    url(r'^Middle/', include(('MiddleWare.urls', 'Middle'))),
    url(r'^Page/', include(('Page.urls', 'Page'))),
    url(r'^CBV/', include(('CBV.urls', 'CBV'))),

    url(r'^DRF/', include(router.urls)),
    url(r'^Cdrf/', include(('CBVDRF.urls', 'CBVDRF'))),

]

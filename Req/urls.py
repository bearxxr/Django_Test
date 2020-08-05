from django.conf.urls import url

from Req import views

urlpatterns = [

    url(r'^test/', views.test),
    url(r'^testRequest/', views.testRequest),

]

from django.conf.urls import url

from Session.views import SessionLoginView,WelcomesessionView,SessionLoginoutView

urlpatterns = [
    url(r'^sessionLogin/', SessionLoginView.as_view(),name='sessionLogin'),
    url(r'^welcomesession/', WelcomesessionView.as_view(),name='welcomesession'),
    url(r'^sessionloginout/', SessionLoginoutView.as_view(),name='sessionloginout'),
]

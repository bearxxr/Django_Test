from django.conf.urls import url

from T import views


urlpatterns = [
    url(r'test/',views.test),

    url(r'testPoint/',views.testPoint),
    url(r'testTag/',views.testTag),
    url(r'getStatic/',views.getStatic),
]
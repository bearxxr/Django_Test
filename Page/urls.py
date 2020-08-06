from django.urls import re_path

from Page import views

urlpatterns = [
    re_path(r'^Djangopage/',views.Djangopage,name='Djangopage'),
]
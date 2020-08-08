from django.urls import re_path

from CBVDRF import views

urlpatterns = [
    re_path(r'^testcbvdrf/', views.TestCbvDrf.as_view(), name='testcbvdrf'),
]

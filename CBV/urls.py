from django.conf.urls import url

from CBV import views

urlpatterns = [
    url(r'^testTempView/', views.TestTempView.as_view(template_name='testTemplateView.html')),
    url(r'^testListView/', views.TestListView.as_view()),
    url(r'^testDetailView/(?P<pk>\d+)/', views.TestDetailView.as_view()),
]

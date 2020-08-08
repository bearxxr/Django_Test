from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from Res.models import Animal


class TestTempView(TemplateView):
    # template_name = 'testTemplateView.html'
    pass


class TestListView(ListView):
    template_name = 'testTemplateView.html'
    # model = Animal
    queryset = Animal.objects.all()


class TestDetailView(DetailView):
    template_name = 'detail.html'
    # model = Animal
    queryset = Animal.objects.all()

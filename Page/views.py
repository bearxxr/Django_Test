from django.core.paginator import Paginator
from django.shortcuts import render

from Page.models import Goods


def Djangopage(request):
    page = request.GET.get('page', 1)
    print(type(page))
    per_page = request.GET.get('per_page', '2')

    # 所有对象
    goods = Goods.objects.all()

    # Paginator对象
    pagin = Paginator(goods, per_page)
    p = pagin.page(page)
    print(p)

    context = {
        'pagin': pagin,
        'p': p,
        'page': int(page)
    }

    return render(request, 'DjangoPage.html', context=context)

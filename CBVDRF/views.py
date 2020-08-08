from django.http import JsonResponse
from django.views import View

from CBVDRF.models import Women
from CBVDRF.serializers import WomenSerializer


class TestCbvDrf(View):
    def get(self, request):
        womens = Women.objects.all()

        womenserializer = WomenSerializer(womens, many=True)

        data = {
            'msg': 'ok',
            'status': 200,
            'women': womenserializer.data
        }

        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})

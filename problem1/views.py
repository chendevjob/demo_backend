import random
import json

from django.utils.decorators import method_decorator
from django.views import View
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from problem1.models import LatestArrayModel, SaveArrayModel

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class LatestArrayView(View):
    def get(self, request):
        array = random.sample(range(1, 101), 10)

        # 只存最新的数据，每次更新
        record = LatestArrayModel.objects.filter().first()
        if record is None:
            record = LatestArrayModel()
        record.array = json.dumps(array)
        record.save()

        return JsonResponse({
            'status': 'SUCCESS',
            'data': {
                'array': array
            }
        })


@method_decorator(csrf_exempt, name='dispatch')
class SaveArrayView(View):
    def get(self, request):
        # 最多返回100条
        arrays = []
        for item in SaveArrayModel.objects.filter().order_by('-id')[:100]:
            save_time = item.created_time.strftime('%Y-%m-%d %H:%M:%S')
            array = json.loads(item.array)
            arrays.append({
                'save_time': save_time,
                'array': array
            })

        return JsonResponse({
            'status': 'SUCCESS',
            'data': {
                'arrays': arrays
            }
        })

    def post(self, request):
        post_data = json.loads(request.body)
        array = json.dumps(post_data['array'])
        record = SaveArrayModel()
        record.array = array
        record.save()

        return JsonResponse({
            'status': 'SUCCESS'
        })

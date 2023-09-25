import json
from django.http import JsonResponse
from .models import Robot
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


possible_models = ["R2", "R3", "R4", "R5"]
possible_versions = ["D2", "D3", "D4", "D5", "A1", "A2", "A3", "A4"]

@csrf_exempt
def create_robot(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        model = data.get('model')
        version = data.get('version')
        serial = f"{model}-{version}"
        if model not in possible_models or version not in possible_versions:
            return JsonResponse({'message': 'Неверная модель или версия робота'}, status=400)
        created = datetime.now()
        robot = Robot(model=model, version=version, created=created, serial=serial)
        robot.save()

        return JsonResponse({'message': 'Робот создан успешно'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


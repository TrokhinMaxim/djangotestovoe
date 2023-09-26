import json
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone
from django.http import HttpResponse
from openpyxl import Workbook

from .models import Robot

possible_models = ["R2", "R3", "R4", "R5"]
possible_versions = ["D2", "D3", "D4", "D5", "A1", "A2", "A3", "A4"]
one_week_ago = timezone.now() - timezone.timedelta(days=7)

@csrf_exempt
def create_robot(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        model = data.get('model')
        version = data.get('version')
        serial = f"{model}-{version}"
        if model not in possible_models or version not in possible_versions:
            return JsonResponse({'message': 'Неверная модель или версия робота'}, status=400)
        created = data.get('created')
        if created is None:
            created = datetime.datetime.now()
        elif isinstance(created, str):
            created = datetime.datetime.strptime(created, '%Y-%m-%d %H:%M:%S')
            if created > datetime.datetime.now():
                return JsonResponse({'message': 'Дата не может превышать текущую дату'}, status=400)
        robot = Robot(model=model, version=version, created=created, serial=serial)
        robot.save()
        return JsonResponse({'message': 'Робот создан успешно'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


def summary(request):
    robots = Robot.objects.filter(created__gte=one_week_ago).values('model', 'version').annotate(
        week_count=Count('id'))
    template = 'robots/summary.html'
    context = {
        'robots': robots
    }
    return render(request, template, context)

def download_excel_report(request):
    wb = Workbook()
    summary_query = Robot.objects.filter(created__gte=one_week_ago).values('model', 'version').annotate(
        week_count=Count('id'))
    summary_data = list(summary_query)
    summary_dict = {}
    for item in summary_data:
        model = item['model']
        version = item['version']
        count = item['week_count']
        if model not in summary_dict:
            summary_dict[model] = {}
        summary_dict[model][version] = count
    for model, version_data in summary_dict.items():
        ws = wb.create_sheet(title=model)
        ws.append(['Модель', 'Версия', 'Количество за неделю'])
        for version, count in version_data.items():
            ws.append([model, version, count])
    del wb['Sheet']
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=summary_report.xlsx'
    wb.save(response)

    return response

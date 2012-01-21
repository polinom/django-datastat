from django.db.models import get_model, Count
from django.shortcuts import render

def modelstat(request, app_label, model_name):
    Model = get_model(app_label, model_name)
    all = Model.objects.all().values("year").annotate(count=Count("pk")).order_by('-count')
    return render(request, 'datastat/show_chart.html', {'all':all})

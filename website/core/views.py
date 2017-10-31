from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from core.models import VisitorRecord, Article

@csrf_exempt
def visitor(request):
    if request.method == 'POST':
        name = request.POST.get('name') or ''
        phone = request.POST.get('mobile') or ''
        product = request.POST.get('product') or ''
        aim = request.POST.get('aim') or ''
        VisitorRecord(name=name, phone=phone, product=product, aim=aim).save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400, reason='only POST is accepted')
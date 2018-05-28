import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from core.models import VisitorRecord, Article, Category

@csrf_exempt
def visitor(request):
    if request.method == 'POST':
        name = request.POST.get('name') or ''
        phone = request.POST.get('mobile') or request.POST.get('phone')
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if client_ip:
            ip = cip
        else:
            ip = request.META.get('REMOTE_ADDR')
        product = request.POST.get('product') or ''
        aim = request.POST.get('aim') or ''
        VisitorRecord(name=name, phone=phone, product=product, aim=aim, ip=ip).save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400, reason='only POST is accepted')

def studios(request):
    res = list(Article.objects.filter(category__title='画室').values('id', 'desc', 'cover', 'title'))
    return JsonResponse(res, safe=False)
def studios_index(request):
    res = list(Article.objects.filter(category__title='画室', promote=True).values('id', 'desc', 'cover', 'title'))
    return JsonResponse(res, safe=False)

def news(request):
    res = list(Article.objects.filter(category__title='非凡头条').values('id', 'desc', 'cover', 'title'))
    return JsonResponse(res, safe=False)
def news_index(request):
    res = list(Article.objects.filter(category__title='非凡头条', promote=True)[:6].values('id', 'desc', 'cover', 'title'))
    return JsonResponse(res, safe=False)

def article(request, id):
    res = list(Article.objects.filter(pk=id).values('cover', 'title', 'content', 'keyword', 'desc'))
    return JsonResponse(res, safe=False)

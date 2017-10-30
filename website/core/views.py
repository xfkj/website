from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from core.models import VisitorRecord, Article

@csrf_exempt
def visitor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('mobile')
        product = request.POST.get('product')
        article_id = request.POST.get('article_id')
        article = Article.objects.get(pk=article_id)
        VisitorRecord(name=name, phone=mobile, product=product, articleOfInterest=article).save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400, reason='only POST is accepted')
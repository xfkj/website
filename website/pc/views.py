from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from core.models import Article, Category
from django.http import HttpResponse

def home(request):
    data = {}
    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data[cat.title] = articles
    return render_to_response('home.html', data)

def article(request, id=None, title=None, tmpl='article.html'):
    if id is not None:
        obj = get_object_or_404(Article, pk=id)
    else:
        obj = get_object_or_404(Article, title=title)
    return render_to_response(tmpl, obj)
from django.shortcuts import render_to_response
from core.models import Article, Category




# Create your views here.
def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    print(data)
    return render_to_response('mobile/index.html', data)


def article(request, id):
    return render_to_response('mobile/article.html', {'title': '标题', 'desc': '概要', 'content': '内容'})
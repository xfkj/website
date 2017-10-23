from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from core.models import Article, Category




# Create your views here.
def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    return render_to_response('mobile/index.html', data)


def article(request, article_id):
    article_obj = get_object_or_404(Article, pk=article_id)
    return render_to_response('mobile/article.html',
        {
            'article': article_obj
        })



def category(request, category_id):
    category_obj = get_object_or_404(Category, pk=category_id)
    articles = category_obj.article_set.all()
    return render_to_response('mobile/category.html',
        {
            'category': category_obj.title,
            'articles': articles,
        })
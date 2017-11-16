from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from core.models import Article, Category

def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    return render_to_response('pc/home.html', data)

def article(request, article_id=None, article_title=None):
    if article_id is not None:
        article_obj = get_object_or_404(Article, pk=article_id)
    else:
        article_obj = get_object_or_404(Article, title=article_title)
    return render_to_response(get_template_for_article(article_obj),
        {
            'article': article_obj
        })



def category(request, category_id=None, category_title=None):

    if category_id is not None:
        category_obj = get_object_or_404(Category, pk=category_id)
    else:
        category_obj = get_object_or_404(Category, title=category_title)
    articles = category_obj.article_set.all()

    return render_to_response(get_template_for_category(category_obj),
        {
            'category': category_obj,
            'articles': articles,
        })



def get_template_for_category(category):
    cat_name = category.title
    template_map = {
        '非凡名师': 'pc/people.html',
        '优秀学员': 'pc/people.html',
        '校区介绍': 'pc/category.html',
        '非凡头条': 'pc/information.html',
        '非凡战绩': 'pc/category.html',
        '高考冲刺': 'pc/category.html',
    }

    return template_map[cat_name]


def get_template_for_article(article):
    return 'pc/article.html'

def props(obj):  
    pr = {}  
    for name in dir(obj):  
        value = getattr(obj, name)  
        if not name.startswith('__') and not callable(value):
            pr[name] = value  
    return pr  
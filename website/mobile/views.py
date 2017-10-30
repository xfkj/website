from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from core.models import Article, Category

def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    return render_to_response('mobile/index.html', {
    'categories': {
        '课程产品': [
        {
            'id': 1,
            'cover': {'url': '../static/mobile/img/home/banner02.png'},
        },
        {
            'id': 1,
            'cover': {'url': '../static/mobile/img/home/banner02.png'},
        },
        {
            'id': 1,
            'cover': {'url': '../static/mobile/img/home/banner02.png'},
        },
        {
            'id': 1,
            'cover': {'url': '../static/mobile/img/home/banner02.png'},
        },
        ],
        '非凡头条': [
        {
            'id': 1,
            'desc': '非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条',
            'cover': {'url': '../static/mobile/img/home/pt01.png'},
        },
        {
            'id': 1,
            'desc': '非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条',
            'cover': {'url': '../static/mobile/img/home/pt01.png'},
        },
        {
            'id': 1,
            'desc': '非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条',
            'cover': {'url': '../static/mobile/img/home/pt01.png'},
        },
        {
            'id': 1,
            'desc': '非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条非凡头条',
            'cover': {'url': '../static/mobile/img/home/pt01.png'},
        },
        ],
        '非凡名师': [
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },
        {
            'id': 1,
            'name': '王小一',
            'subject':'语文',
            'cover': {'url':'../static/mobile/img/home/teacher1.png'}
        },

        ],
    }

})

def article(request, article_id=None, article_title=None):
    if article_id is not None:
        article_obj = get_object_or_404(Article, pk=article_id)
    else:
        article_obj = get_object_or_404(Article, title=article_title) 
    return render_to_response('mobile/article.html',
        {
            'article': article_obj
        })



def category(request, category_id=None, category_title=None):
    if category_id is not None:
        category_obj = get_object_or_404(Category, pk=category_id)
    else:
        category_obj = get_object_or_404(Category, title=category_title)
    articles = category_obj.article_set.all()
    return render_to_response('mobile/category.html',
        {
            'category': category_obj.title,
            'articles': articles,
        })

def signUp(request):
    return render_to_response('mobile/signUp.html')

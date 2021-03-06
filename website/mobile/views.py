from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from core.models import Article, Category

def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    return render_to_response('mobile/index.html', data)

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
    article_id = request.GET.get('article_id')
    article_obj = None
    if article_id is not None:
        article_obj = get_object_or_404(Article, pk=article_id)

    if category_id is not None:
        category_obj = get_object_or_404(Category, pk=category_id)
    else:
        category_obj = get_object_or_404(Category, title=category_title)
    articles = category_obj.article_set.all()

    if article_obj is None:
        article_obj = articles[0]

    tags = extract_tags(articles)
    return render_to_response(get_template_for_category(category_obj),
        {
            'category': category_obj.title,
            'tags': tags,
            'articles': articles,
            'top_article': article_obj,
            'id': article_id
        })

def myfz(request):
    return redirect('//m.myfz.ffjy.org')

def get_template_for_category(category):
    cat_name = category.title
    template_map = {
        '非凡名师': 'mobile/teachers.html',
        '礼包': 'mobile/goAndGet.html',
        '优秀学员': 'mobile/students.html',
        '校区介绍': 'mobile/campus.html',
        '非凡头条': 'mobile/topArticles.html',
        '非凡战绩': 'mobile/militaryExploits.html',
        '高考冲刺': 'mobile/nEMT.html',
    }

    return template_map[cat_name]


def get_template_for_article(article):
    template_map = {
        '非凡名师': 'mobile/masterDetails.html',
        '优秀学员': 'mobile/studentDetails.html',
        '礼包': 'mobile/receive.html',
        '非凡头条': 'mobile/topArticleDetails.html',
        '课程产品': 'mobile/optional.html',
        '普通文章': 'mobile/about.html',
        '高考冲刺': 'mobile/optional.html',
    }
    return template_map[article.category.title]

def extract_tags(articles):
    return list(set([article.tags.all()[0] for article in articles]))

def signUp(request):
    return render_to_response('mobile/signUp.html')

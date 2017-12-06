from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from core.models import Article, Category, Tag


def home(request):
    data = {}
    data['categories'] = {}

    categories = Category.objects.all()
    for cat in categories:
        articles = cat.article_set.filter(promote=True)
        data['categories'][cat.title] = articles
    return render_to_response('pc/home.html', data)


def article(request, article_id=None, article_uri=None):
    recommends = Article.objects.filter(is_recommend=True)
    if article_id is not None:
        article_obj = get_object_or_404(Article, pk=article_id)
    else:
        article_obj = get_object_or_404(Article, uri=article_uri)
    return render_to_response(get_template_for_article(article_obj),
        {
            'article': article_obj,
            'recommends': recommends
        })


def category(request, category_id=None, category_uri=None):

    if category_id is not None:
        category_obj = get_object_or_404(Category, pk=category_id)
    else:
        category_obj = get_object_or_404(Category, uri=category_uri)
    articles = category_obj.article_set.all()

    tags = extract_tags(articles)
    tag_string = request.GET.get('tag', '')
    if tag_string != '':
        articles = articles.filter(tags__tag=tag_string)

    return render_to_response(
        get_template_for_category(category_obj), {
            'tag': tag_string,
            'tags': tags,
            'category': category_obj,
            'articles': articles,
        })


def get_template_for_category(category):
    cat_name = category.title
    DEFAULT_TEMPLATE = "pc/category.html"
    template_map = {
        '非凡名师': 'pc/people.html',
        '优秀学员': 'pc/people.html',
        '非凡战绩': 'pc/people.html',
        '非凡头条': 'pc/information.html',
        '上分学堂': 'pc/shangfenxuetang.html',
    }

    return cat_name in template_map and template_map[cat_name] or DEFAULT_TEMPLATE


def get_template_for_article(article):
    return 'pc/article.html'

def extract_tags(articles):
    return list(set([article.tags.all()[0] for article in articles]))

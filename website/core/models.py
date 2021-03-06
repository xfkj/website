from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone as django_tz
from .empty_checker import EMPTYChecker
from uuslug import slugify

class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='分类')
    uri = models.CharField(max_length=200, blank=True)
    cover = models.ImageField(verbose_name='封面', default=models.ImageField())

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.uri = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    tag = models.CharField(max_length=30, verbose_name='标签')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


# Create your models here.
class Article(models.Model):
    area = models.CharField(max_length=50, verbose_name='地区', default="杭州")
    title = models.CharField(max_length=100, verbose_name='标题')
    uri = models.CharField(max_length=200, blank=True)
    keyword = models.CharField(max_length=200, verbose_name='关键词',blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    desc = models.TextField(verbose_name='概要')
    cover = models.ImageField(verbose_name='封面')
    content = models.TextField(verbose_name='正文')
    pc_content = models.TextField(
        verbose_name="pc端正文(如果和移动端不一样，可以录入在这里)", null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name='分类', on_delete=models.PROTECT)
    promote = models.BooleanField(verbose_name='置于首页')
    is_recommend = models.BooleanField(verbose_name='设为推荐', default=False)
    weight = models.IntegerField(verbose_name='排序')

    def save(self,*args, **kwargs):
        self.pc_content = self.__filterEmptyHTML(self.pc_content)
        self.uri = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __filterEmptyHTML(self, input):
        if input:
            parser = EMPTYChecker()
            parser.feed(input)
            if parser.is_empty:
                return ''
        return input

    def image_tag(self):
        return mark_safe(u'<img class="cover" src="%s" />' % self.cover.url)

    image_tag.short_description = '封面预览'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['weight']


class VisitorRecord(models.Model):
    name = models.CharField(max_length=100, verbose_name='访客姓名')
    phone = models.CharField(max_length=30, verbose_name='电话')
    ip = models.CharField(max_length=30, verbose_name='ip', default='')
    product = models.CharField(
        max_length=100, verbose_name='选择的产品', blank=True)
    aim = models.CharField(max_length=100, verbose_name='来源', blank=True)
    created_at = models.DateTimeField(
        default=django_tz.now, verbose_name='提交时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '访客'
        verbose_name_plural = '访客'

class Seo(models.Model):
    site_name = models.CharField(max_length=300, verbose_name='网站名称',default='非凡教育')
    title = models.CharField(max_length=300, verbose_name='首页标题')
    keyword = models.CharField(max_length=300, verbose_name='首页keyword')
    description = models.CharField(max_length=500, verbose_name='首页description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'

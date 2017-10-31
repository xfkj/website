from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone as django_tz


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='分类')


    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=100, verbose_name='标题')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    desc = models.TextField(verbose_name='概要')
    cover = models.ImageField(verbose_name='封面')
    content = models.TextField(verbose_name='正文')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    promote = models.BooleanField(verbose_name='置于首页')
    weight = models.IntegerField(verbose_name='排序')


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
    product = models.CharField(max_length=100, verbose_name='选择的产品', blank=True)
    aim = models.CharField(max_length=100, verbose_name='来源', blank=True)
    created_at = models.DateTimeField(default=django_tz.now, verbose_name='提交时间')


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = '访客'
        verbose_name_plural = '访客'
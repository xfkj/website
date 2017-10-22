from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='分类')


    def __str__(self):
        return self.title




class Tag(models.Model):
    tag = models.CharField(max_length=30, verbose_name='标签')


    def __str__(self):
        return self.tag




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


    def __str__(self):
        return self.title




class VisitorRecord(models.Model):
    name = models.CharField(max_length=100, verbose_name='访客姓名')
    phone = models.CharField(max_length=30, verbose_name='电话')
    articleOfInterest = models.ForeignKey(Article, verbose_name='感兴趣的文章', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

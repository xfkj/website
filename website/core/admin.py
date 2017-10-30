from django.contrib import admin
from .models import Article, VisitorRecord, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

for m in [VisitorRecord, Category, Tag]:
    admin.site.register(m)


class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title',
        'category',
        'promote',
        'weight',
    )
    list_display_links = ('title', )
    list_editable = ('category', 'promote', 'weight')
    list_filter = ('category', 'promote', 'tags')
    readonly_fields = ('image_tag',)



admin.site.register(Article, ArticleAdmin)
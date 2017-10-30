from django.contrib import admin
from .models import Article, VisitorRecord, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

for m in [VisitorRecord, Category, Tag]:
    admin.site.register(m)


class SummernoteAdmin(SummernoteModelAdmin):
    pass



admin.site.register(Article, SummernoteAdmin)
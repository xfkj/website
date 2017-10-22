from django.contrib import admin
from .models import Article, VisitorRecord, Category, Tag
# Register your models here.

for m in [Article, VisitorRecord, Category, Tag]:
    admin.site.register(m)

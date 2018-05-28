from django import forms
from django.contrib import admin
from .models import Article, VisitorRecord, Category, Tag, Seo
from django_summernote.widgets import SummernoteWidget


# Register your models here.

for m in [Category, Tag]:
    admin.site.register(m)


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'content': SummernoteWidget(),
            'pc_content': SummernoteWidget(),
        }
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = (
        'title',
        'category',
        'promote',
        'is_recommend',
        'weight',
    )
    list_display_links = ('title', )
    list_editable = ('category', 'promote', 'is_recommend', 'weight')
    list_filter = ('area', 'category', 'promote', 'tags')
    readonly_fields = ('image_tag',)



admin.site.register(Article, ArticleAdmin)




class VisitorAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ('name', 'phone', 'product', 'aim', 'ip', 'created_at')

    def has_add_permission(self, request):
        return False


admin.site.register(VisitorRecord, VisitorAdmin)

class SeoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'title', 'keyword', 'description')

admin.site.register(Seo, SeoAdmin)

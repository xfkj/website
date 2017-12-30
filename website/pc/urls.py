from pc import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='pc_home'),
    path('article/<int:article_id>/', views.article, name='pc_article'),
    path('category/<int:category_id>/', views.category, name='pc_category'),
    path('article/<str:article_uri>/', views.article, name='pc_article_by_uri'),
    path('category/<str:category_uri>/', views.category, name='pc_category_by_uri'),
    path('studio', views.studio, name='studio'),
    path('baidu_verify_GCKa1DpkNw.html', views.baidu)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from mobile import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signUp', views.signUp, name='signUp'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('article/<str:article_title>/', views.article, name='article_by_title'),
    path('category/<str:category_title>/', views.category, name='category_by_title'),
    path('myfz', views.myfz)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from mobile import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signUp', views.signUp, name='signUp'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('category/<int:category_id>/', views.category, name='category'),
]

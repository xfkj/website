from mobile import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('category/<int:category_id>/', views.category, name='category'),
]
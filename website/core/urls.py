from django.urls import path
from core import views

urlpatterns = [
    path('api/visitors', views.visitor),
    path('studios', views.studios),
    path('studios/index', views.studios_index),
    path('news', views.news),
    path('news/index', views.news_index),
    path('articles/<int:id>', views.article),
]

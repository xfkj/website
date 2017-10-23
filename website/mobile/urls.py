from mobile import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article, name='article'),
]
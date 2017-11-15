from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/<str:tmpl>', views.article, name='article'),
    # path('article/<str:title>/<str:tmpl>', views.article, name='article'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
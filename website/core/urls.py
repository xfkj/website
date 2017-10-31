from django.urls import path
from core import views

urlpatterns = [
    path('api/visitors', views.visitor),
]

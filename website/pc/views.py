from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from core.models import Article, Category
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.http import HttpResponse
from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, template_name='news/index.html', context={'news': news, 'title': 'Список новостей'})


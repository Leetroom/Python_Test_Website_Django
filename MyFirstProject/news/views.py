from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category

def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    return render(request, template_name='news/index.html', context={'news': news, 'title': 'Список новостей', 'categories': categories})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html',context={'news': news, 'title': 'Список новостей', 'categories': categories, 'category': category})
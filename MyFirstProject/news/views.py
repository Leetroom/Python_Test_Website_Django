from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    return render(request, template_name='news/index.html', context={'news': news, 'title': 'Список новостей',})

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html',context={'news': news, 'title': 'Список новостей', 'category': category})
def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
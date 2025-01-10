from django.shortcuts import render
from .models import News, Service


# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import News

def newsDetail(request, slug):
    news = get_object_or_404(News, slug=slug)  # Fetch the news item by slug
    return render(request, 'news_detail.html', {'news': news})


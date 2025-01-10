from django.urls import path
from . import views
from news.models import News




urlpatterns = [
    path('', views.home, name='home'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),  # Detail page for each news item
]

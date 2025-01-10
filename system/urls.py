"""
URL configuration for system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('course/', views.course, name='course'),
    path('calculator/', views.calculator, name='calculator'),
    path('userform/', views.UsersFormView, name='userform'),
    path('numbercheck/', views.check_number_view, name='numbercheck'),
    path('marksheet/', views.marksheet_view, name='marksheet'),
    path('manual-form/', views.manual_form_view, name='manual_form'),
]






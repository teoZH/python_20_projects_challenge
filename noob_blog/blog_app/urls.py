from django.urls import path

from blog_app import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('articles/', views.articles, name='article')
]
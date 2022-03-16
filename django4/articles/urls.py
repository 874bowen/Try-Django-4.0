from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('article/create/', views.ArticleCreate.as_view(), name='article_create')
]
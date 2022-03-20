from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('register/', views.register_view, name='register'),
    path('create/', views.ArticleCreate.as_view(), name='article_create'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='article_update'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(), name='article_delete'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('form/', views.ArticleFormView.as_view(), name="article_form"),
]
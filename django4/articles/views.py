import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Article
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class HomeView(View):

    def get(self, request):

        article_obj = Article.objects.get(id=1)
        count = Article.objects.all().count()
        articles = Article.objects.all()
        ctx = {"articles_list": articles, "articles_count": count}

        return render(request, 'articles/article_list.html', ctx)

class ArticleCreate(CreateView):

    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')
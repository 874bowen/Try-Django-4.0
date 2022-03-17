import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView

from .models import Article
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
# def ArticleSearch(request):
#     print(request)
#     query_dict = request.GET
#     print(query_dict)
#     q = query_dict.get("query")
#     print(q)
#     try:
#         query = int(query_dict.get("query"))
#         print(query)
#     except:
#         query = None
#
#     if query is not None:
#         article = Article.objects.get(id=query)
#
#     context = {"article": article}
#     return render(request, "articles/article_search.html", context)
#

class HomeView(View):

    def get(self, request):
        # print(request.user)
        article_obj = Article.objects.get(id=1)
        count = Article.objects.all().count()
        articles = Article.objects.all()
        ctx = {"articles_list": articles, "articles_count": count}

        return render(request, 'articles/article_list.html', ctx)


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from .models import Article
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import ArticleForm


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


class ArticleFormView(FormView, View):
    template_name = 'articles/article_form_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articles:all')

    # def get(self, request):
    #     form = ArticleForm(request.POST or None)
    #     ctx = {"form": form}
    #     if form.is_valid():
    #         article_obj = form.save()
    #         ctx["form"] = ArticleForm()\
    def form_valid(self, form):
        data = form.clean()
        title = data.get("title")
        content = data.get("content")
        objectArt = Article(title=title, content=content)
        objectArt.save()

        # b = Article(data)
        # b.save()
        return super().form_valid(form)


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:article_create')


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

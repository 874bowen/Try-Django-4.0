import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import ArticleForm


# Create your views here.

class HomeView(View):

    def get(self, request):
        # print(request.user)
        article_obj = Article.objects.get(id=1)
        count = Article.objects.all().count()
        articles = Article.objects.all()
        ctx = {"articles_list": articles, "articles_count": count}

        return render(request, 'articles/article_list.html', ctx)


# class RegisterView(View):

def register_view(request):
    form = UserCreationForm(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        user_obj = form.save()
        return HttpResponseRedirect(reverse('articles:all'))

    return render(request, 'registration/registration.html', ctx)


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

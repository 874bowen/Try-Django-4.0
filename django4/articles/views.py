import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import ArticleForm


# Create your views here.
from .owner import OwnerListView, OwnerDeleteView, OwnerDetailView, OwnerCreateView


def register_view(request):
    form = UserCreationForm(request.POST or None)
    ctx = {"form": form}
    if form.is_valid():
        user_obj = form.save()
        return HttpResponseRedirect(reverse('articles:all'))

    return render(request, 'registration/registration.html', ctx)


class HomeView(OwnerListView):
    model = Article

    # def get(self, request):
    #     # print(request.user)
    #     article_obj = Article.objects.get(id=1)
    #     count = Article.objects.all().count()
    #     articles = Article.objects.all()
    #     ctx = {"articles_list": articles, "articles_count": count}
    #
    #     return render(request, 'articles/article_list.html', ctx)


class ArticleFormView(FormView, View):
    template_name = 'articles/article_form_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articles:all')

    def form_valid(self, form):
        data = form.clean()
        title = data.get("title")
        content = data.get("content")
        objectArt = Article(title=title, content=content)
        objectArt.save()

        return super().form_valid(form)


class ArticleCreate(OwnerCreateView):
    model = Article

    fields = ['title', 'content']
    # fields = "__all__"
    success_url = reverse_lazy('articles:all')



class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')


class ArticleDelete(OwnerDeleteView, DeleteView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy('articles:all')


class ArticleDetail(OwnerDetailView, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

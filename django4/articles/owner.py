from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article


class OwnerListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerDetailView(DetailView):
    """
    Sub-class the ListView to pass the request to the form.
    """


class OwnerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Sub-class the ListView to pass the request to the form.
    """

    def form_valid(self, form):
        print("form_valid called")
        object_art = form.save(commit=False)
        object_art.owner = self.request.user
        object_art.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the ListView to pass the request to the form.
    """

    def get_queryset(self):
        print('get_queryset called')
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)

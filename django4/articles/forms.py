from django.forms import ModelForm
from .models import Article
from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.all().filter(title__icontains = title)
        if qs.exists():
            self.add_error("title", f"{title} is taken")
        return data


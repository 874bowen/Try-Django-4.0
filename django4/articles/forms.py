from django.forms import ModelForm
from .models import Article

class MakeForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
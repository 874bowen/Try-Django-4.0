from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify


# Create your models here.

class Article(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Enter Title e.g., Python, Hello World",
        validators=[MinLengthValidator(3, 'Title must be greater than three')]
    )
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

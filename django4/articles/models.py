from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.signals import pre_save, post_save
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
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def slugify_instance_title(instance, save=False):
        slug = slugify(instance.title)
        qs = Article.objects.filter(slug=slug).exclude(id=instance.id)
        if qs.exists():
            slug = f"{slug}-{qs.count()+1}"
        instance.slug = slug
        if save:
            instance.save()
        return instance

    def article_pre_save(sender, instance, *args, **kwargs):
        print('pre save')
        if instance.slug is None:
            sender.slugify_instance_title(instance, save=False)

    pre_save.connect(article_pre_save, sender=super())

    def article_post_save(sender, instance, created, *args, **kwargs):
        print('post save')
        if created:
            sender.slugify_instance_title(instance, save=True)

    post_save.connect(article_pre_save, sender=super())
    #

    def __str__(self):
        return self.title

from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Enter Title e.g., Python, Hello World",
        validators=[MinLengthValidator(3, 'Title must be greater than three')]
    )
    content = models.TextField()

    def __str__(self):
        return self.title
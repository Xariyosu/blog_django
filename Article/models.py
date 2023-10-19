from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    content = models.TextField(blank=False, null=False)
    priority = models.BooleanField(default=False)

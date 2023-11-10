from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    content = models.TextField(blank=False, null=False)
    priority = models.BooleanField(default=False)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


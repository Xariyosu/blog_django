from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    priority = models.BooleanField(default=False)

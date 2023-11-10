from django.shortcuts import render, get_object_or_404, redirect

from .models import Article

from .forms import ArticleForm


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "articles/article_list.html", context)

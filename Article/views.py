from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Comment
from django.views.generic.edit import CreateView

from .forms import ArticleForm


def article_list_view(request):
    articles = Article.objects.all().order_by('-priority')
    comments = Comment.objects.all().order_by('-created_at')
    context = {
        'object_list': articles,
        'comments': comments
    }
    return render(request, "articles/article_list.html", context)


def add_comment(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        author = request.POST.get('author')
        content = request.POST.get('content')

        article = get_object_or_404(Article, pk=article_id)

        Comment.objects.create(
            article=article,
            author=author,
            content=content,
        )

    return redirect('article-list')


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'author', 'content', 'priority']


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')  # Assuming you have a URL named 'article-list'
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import ArticleForm, OptionForComments


def article_list_view(request):
    articles = Article.objects.all().order_by('-priority', '-created_at')
    comments = Comment.objects.all().order_by('-created_at')
    k_comments = []
    seen_articles = set()

    for comment in comments:
        article_id = comment.article_id
        if article_id not in seen_articles:
            seen_articles.add(article_id)
            k_comments.append(comment)
    context = {
        'object_list': articles,
        'comments': k_comments
    }
    return render(request, "articles/article_list.html", context)


def article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.all().filter(article=article.id).order_by('-created_at')
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'articles/article.html', context)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.article_id
    if request.method == 'POST':
        comment.delete()
        return redirect('article', article_id)

    return render(request, 'articles/delete_comment.html', {'comment': comment})


@login_required
def add_comment(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        author = request.user
        content = request.POST.get('content')

        article = get_object_or_404(Article, pk=article_id)

        Comment.objects.create(
            article=article,
            author=author,
            content=content,
        )

    return redirect('article', article_id)


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'content', 'priority']


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article-list')
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})


def all_comments(request):
    # users = User.objects.all()

    if request.method == 'GET':
        form = OptionForComments(request.GET)
        # form.files['filter_option'].choices = [(user.id, user.username) for user in users]

        if form.is_valid():
            selected_user_id = form.cleaned_data['filter_option']
            if selected_user_id:
                comments = Comment.objects.filter(author__id=selected_user_id).order_by('-created_at')
                for a in comments:
                    print(a)
            else:
                comments = Comment.objects.order_by('-created_at')

        else:
            comments = Comment.objects.order_by('-created_at')
    else:
        form = OptionForComments()
        comments = Comment.objects.order_by('-created_at')

    context = {
        'comments': comments,
        'form': form
    }

    return render(request, 'articles/all_comments.html', context)

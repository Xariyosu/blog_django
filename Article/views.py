from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Comment
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import ArticleForm, OptionForComments


def article_list_view(request):
    articles = Article.objects.all().order_by('-priority', '-created_at')
    comments = Comment.objects.all().order_by('-created_at')
    context = {
        'object_list': articles,
        'comments': comments
    }
    return render(request, "articles/article_list.html", context)


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

    return redirect('article-list')


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/create_article.html'
    fields = ['title', 'content', 'priority']


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

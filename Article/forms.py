from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class": "article-title",
                "placeholder": "Your title"
            }
        )
    )

    author = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class": "article-author",
                "placeholder": "Article's author"
            }
        )
    )

    content = forms.Textarea(
        attrs={
            "class": "article-content",
            "rows": 20,
            "cols": 120
        }
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'content'
        ]
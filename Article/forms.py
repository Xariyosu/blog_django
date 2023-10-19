from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
            }
        )
    )
    author = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Article's author"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "article-content",
                "rows": 20,
                "cols": 120
            }
        )
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'content'
        ]

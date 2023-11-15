from django import forms

from .models import Article
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your title"
            }
        )
    )
    # author = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Article's author",
    #         }
    #     ),
    # )
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
            'content',
            'priority'
        ]


class OptionForComments(forms.Form):
    users = User.objects.all()
    CHOICES = [(user.id, user.username) for user in users]
    default_user = users.first()
    initial_value = default_user.id if default_user else None
    filter_option = forms.ChoiceField(
        choices=[('', 'Select a user (All comments)')] + CHOICES,
        required=False,
        initial=initial_value
    )

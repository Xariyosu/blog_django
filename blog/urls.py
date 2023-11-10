"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from Article.views import article_list_view, add_comment, ArticleCreateView, add_article

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', article_list_view, name='article-list'),
    path('add_comment/', add_comment, name='add_comment'),
    path('create_article/', ArticleCreateView.as_view(), name='create_article'),
    path('add_article/', add_article, name='add_article'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
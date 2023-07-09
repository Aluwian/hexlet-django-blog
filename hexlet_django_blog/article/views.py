from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from hexlet_django_blog.article.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


def index(request, tags='python', article_id=42):
    return render(request, 'articles.html', context={
        'article_id': article_id,
        'tags': tags
    })

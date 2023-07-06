from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class IndexArticlesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hexlet-django-blog')


def index(request, tags='python', article_id=42):
    return render(request, 'articles.html', context={
        'article_id': article_id,
        'tags': tags
    })

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'articles.html',
        context={
            'name': 'hexlet-django-blog'
        }
    )

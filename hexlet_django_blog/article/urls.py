from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, CommentArticleView

from hexlet_django_blog.article import views

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('comment/', CommentArticleView.as_view(), name='comment_create'),
]

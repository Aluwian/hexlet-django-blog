from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, CommentArticleView, ArticleFormCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view()),
    path('comment/', CommentArticleView.as_view(), name='comment_create'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]

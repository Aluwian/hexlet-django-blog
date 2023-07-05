from django.http import HttpResponse
from django.views import View


# Create your views here.

class IndexArticlesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hexlet-django-blog')

# def index(request):
#     return render(
#         request,
#         'articles.html',
#         context={
#             'name': 'hexlet-django-blog'
#         }
#     )

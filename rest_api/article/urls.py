from django.conf.urls import url

from .views import ArticleView,AuthorView
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = "articles"

urlpatterns = [
    url('articles/', ArticleView.as_view(),name='articles'),
    url('articles/<int:pk>/', ArticleView.as_view()),
    url('authors/', AuthorView.as_view(),name='authors'),
    url('authors/<int:pk>/', AuthorView.as_view()),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
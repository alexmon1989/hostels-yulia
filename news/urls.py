from django.conf.urls import url

from news.views import NewsList, NewsDetailView

app_name = 'news'

urlpatterns = [
    url(r'^$', NewsList.as_view(), name='news_index'),
    url(r'^(?P<pk>[0-9]+)/$', NewsDetailView.as_view(), name='news_detail'),
]

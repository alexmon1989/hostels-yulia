from django.views.generic import ListView, DetailView
from news.models import News


class NewsList(ListView):
    """Отображает список новостей."""
    model = News
    queryset = News.objects.filter(is_published=True)
    paginate_by = 5


class NewsDetailView(DetailView):
    """Отображает новость."""
    queryset = News.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['another_news'] = News.objects.order_by('-created_at').exclude(
            pk=self.kwargs['pk']
        ).filter(is_published=True)[:3]
        return context

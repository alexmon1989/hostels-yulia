from django.views.generic import DetailView
from hostels.models import Hostel


class HostelDetailView(DetailView):
    """Отображает страницу хостела."""
    queryset = Hostel.objects.filter(is_published=True)

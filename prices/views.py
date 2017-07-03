from django.shortcuts import render
from hostels.models import Hostel


def index(request):
    """Отображает страницу цен."""
    hostels = Hostel.objects.filter(is_published=True).order_by('pk')[:3]

    return render(
        request,
        'prices/index.html',
        {
            'hostels': hostels,
        }
    )

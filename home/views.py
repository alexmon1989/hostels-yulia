from django.shortcuts import render
from hostels.models import Hostel
from home.models import Service, AboutUs
from feedbacks.models import Feedback


def index(request):
    """Отображает главную страницу."""
    services = Service.objects.filter(is_published=True).order_by('pk')[:3]
    hostels = Hostel.objects.filter(is_published=True).order_by('pk')[:3]
    about = AboutUs.objects.get()
    feedbacks = Feedback.objects.filter(is_moderated=True, is_published=True, is_on_main_page=True).order_by('pk')[:2]

    return render(
        request,
        'home/index.html',
        {
            'hostels': hostels,
            'services': services,
            'about': about,
            'feedbacks': feedbacks,
        }
    )


def error_404(request):
    return render(
        request,
        'error404.html',
        status=404
    )

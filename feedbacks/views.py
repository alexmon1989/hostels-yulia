from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm


class FeedbacksList(ListView):
    """Отображает список новостей."""
    model = Feedback
    queryset = Feedback.objects.filter(is_moderated=True, is_published=True).order_by('-created_at')
    paginate_by = 4

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FeedbacksList, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = Feedback(
                client_name=request.POST['client_name'],
                position=request.POST['position'],
                text=request.POST['text']
            )
            if request.FILES.get('image'):
                feedback.image = request.FILES['image']
            feedback.save()
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'errors': form.errors}, status=422)

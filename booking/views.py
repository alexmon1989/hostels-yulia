from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import mail_managers
from django.template import loader

from booking.forms import BookingForm


@require_POST
@csrf_exempt
def create_booking(request):
    form = BookingForm(request.POST)
    if form.is_valid():
        # Создание записи в БД
        form.save()

        # Отправка на почту
        html_message = loader.render_to_string(
            'booking/emails/booking.html',
            {
                'name': request.POST['name'],
                'telephone': request.POST['telephone'],
                'email': request.POST['email'],
                'message': request.POST['message'],
            }
        )
        mail_managers('Сообщение клиента с сайта', '', fail_silently=False, html_message=html_message)

        return JsonResponse({'success': 1})
    else:
        return JsonResponse({'errors': form.errors}, status=422)

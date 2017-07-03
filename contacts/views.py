from django.shortcuts import render
from hostels.models import Hostel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import mail_managers
from django.template import loader

from contacts.forms import ContactsForm


@csrf_exempt
def index(request):
    """Отображает страницу контактов. Обрабатывает отправку формы."""
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            html_message = loader.render_to_string(
                'contacts/email/contacts.html',
                {
                    'name': request.POST['name'],
                    'email': request.POST['email'],
                    'subject': request.POST['subject'],
                    'message': request.POST['message'],
                }
            )
            mail_managers('Сообщение клиента с сайта', '', fail_silently=False, html_message=html_message)
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'errors': form.errors}, status=422)
    else:
        hostels = Hostel.objects.filter(is_published=True).order_by('pk')[:3]
        return render(request, 'contacts/index.html', {'hostels': hostels})

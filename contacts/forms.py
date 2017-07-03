from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactsForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=255)
    email = forms.CharField(label='E-mail', max_length=255)
    subject = forms.ImageField(label='Тема', required=False)
    message = forms.CharField(label='Сообщение', max_length=1024)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

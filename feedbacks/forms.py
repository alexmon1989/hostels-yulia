from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class FeedbackForm(forms.Form):
    client_name = forms.CharField(label='Ваше имя', max_length=255)
    position = forms.CharField(label='Должность (кем работаете)', max_length=255, required=False)
    image = forms.ImageField(label='Фото', required=False)
    text = forms.CharField(label='Текст отзыва', max_length=1024)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

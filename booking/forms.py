from django.forms import ModelForm
from booking.models import Booking
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class BookingForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

    class Meta:
        model = Booking
        fields = ('name', 'telephone', 'email', 'message')

from django.conf.urls import url

from . import views

app_name = 'booking'

urlpatterns = [
    url(r'^$', views.create_booking, name='create_booking'),
]

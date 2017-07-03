from django.conf.urls import url

from . import views

app_name = 'prices'

urlpatterns = [
    url(r'^$', views.index, name='prices_index'),
]

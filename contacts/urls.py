from django.conf.urls import url

from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.index, name='contacts_index'),
]

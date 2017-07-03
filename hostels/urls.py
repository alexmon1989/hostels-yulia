from django.conf.urls import url

from hostels.views import HostelDetailView

app_name = 'hostels'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', HostelDetailView.as_view(), name='hostel_details'),
]

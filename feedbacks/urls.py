from django.conf.urls import url

from feedbacks.views import FeedbacksList

app_name = 'feedbacks'

urlpatterns = [
    url(r'^$', FeedbacksList.as_view(), name='feedback_index'),
]

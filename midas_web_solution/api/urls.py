from django.conf.urls import url

from api.eating.views import EatingAPIView 
from api.date.views import DateAPIView


urlpatterns = [
    url(r'^eating/$', EatingAPIView.as_view()),
    url(r'^date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', DateAPIView.as_view()),
]

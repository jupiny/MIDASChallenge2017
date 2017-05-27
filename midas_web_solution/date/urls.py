from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', DateDetailView.as_view(), name='detail'),
]

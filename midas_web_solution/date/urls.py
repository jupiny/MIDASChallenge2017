from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', DateDetailView.as_view(), name='detail'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/meal/', include('meal.urls', namespace='meal')),
]

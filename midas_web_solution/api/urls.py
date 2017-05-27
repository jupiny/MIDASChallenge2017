from django.conf.urls import url

from api.eating.views import EatingAPIView 
from api.date.views import UserDateAPIView, AdminDateAPIView


urlpatterns = [
    url(r'^eating/$', EatingAPIView.as_view()),
    url(r'^user/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', UserDateAPIView.as_view()),
    url(r'^admin/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', AdminDateAPIView.as_view()),
]

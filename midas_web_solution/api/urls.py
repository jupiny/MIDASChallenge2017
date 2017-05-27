from django.conf.urls import url

from api.eating.views import EatingAPIView 


urlpatterns = [
    url(r'^eating/$', EatingAPIView.as_view()),
]

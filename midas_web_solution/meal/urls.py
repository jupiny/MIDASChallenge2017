from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^breakfast/$', CreateBreakfastView.as_view(), name='create_breakfast'),
    url(r'^lunch/$', CreateLunchView.as_view(), name='create_lunch'),
    url(r'^dinner/$', CreateDinnerView.as_view(), name='create_dinner'),
]

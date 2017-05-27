from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', FoodListView.as_view(), name='list'),
    url(r'^new/$', FoodNewView.as_view(), name='new'),
    url(r'^create/$', FoodCreateView.as_view(), name='create'),
]

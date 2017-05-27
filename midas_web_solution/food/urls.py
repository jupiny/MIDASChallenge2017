from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', FoodListView.as_view(), name='list'),
    url(r'^new/$', FoodNewView.as_view(), name='new'),
    url(r'^create/$', FoodCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', FoodDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', FoodEditView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/update/$', FoodUpdateView.as_view(), name='update'),
]

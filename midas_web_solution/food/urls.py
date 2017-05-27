from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', FoodListView.as_view(), name='list'),
]

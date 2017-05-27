from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^breakfast/$', BreakfastCreateView.as_view(), name='create_breakfast'),
    url(r'^lunch/$', LunchCreateView.as_view(), name='create_lunch'),
    url(r'^dinner/$', DinnerCreateView.as_view(), name='create_dinner'),
    url(r'^(?P<meal_id>\d+)/delete/$', MealDeleteView.as_view(), name='delete'),
    url(r'^(?P<meal_id>\d+)/update/$', MealUpdateView.as_view(), name='update'),
]

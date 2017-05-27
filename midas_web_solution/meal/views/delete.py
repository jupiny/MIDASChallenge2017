from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse

from meal.models import Meal 
from date.models import Date
from users.mixins import AdminRequiredMixin


class MealDeleteView(AdminRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        meal_id = kwargs.get('meal_id')
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date = get_object_or_404(Date, date=date)
        meal = get_object_or_404(Meal, pk=meal_id)
        meal.delete()
        return redirect(
            reverse(
                'date:detail',
                kwargs={
                    'year': year,
                    'month': month,
                    'day': day,
                }
            )
        )


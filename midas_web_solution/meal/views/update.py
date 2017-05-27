from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse

from meal.models import Meal 
from date.models import Date
from food.models import Food
from menu.models import Menu 
from users.mixins import AdminRequiredMixin


RICE = 1
SOUP = 2
SIDE_DISH = 3
DESSERT = 4


class MealUpdateView(AdminRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        meal_id = kwargs.get('meal_id')
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date = get_object_or_404(Date, date=date)
        meal = get_object_or_404(Meal, pk=meal_id)
        return render(
            request,
            'meal/edit.html',
            context={
                'rice_set': Food.objects.filter(food_type=RICE),
                'soup_set': Food.objects.filter(food_type=SOUP), 'side_dish_set': Food.objects.filter(food_type=SIDE_DISH),
                'meal': meal,
                'year': year,
                'month': month,
                'day': day,
             }
        )

    def post(self, request, *args, **kwargs):
        meal_id = kwargs.get('meal_id')
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day

        rice_id = request.POST.get('rice')
        soup_id = request.POST.get('soup')
        new_side_dish_id_set = request.POST.getlist('side_dish')
        new_side_dish_id_set = list(map(lambda x: int(x), new_side_dish_id_set))

        date = get_object_or_404(Date, date=date)
        meal = get_object_or_404(Meal, pk=meal_id)

        if rice_id != meal.rice.id:
            menu = Menu.objects.get(
                meal_id=meal.id,
                food_id=meal.rice.id,
            )
            menu.food_id = rice_id
            menu.save()

        if soup_id != meal.soup.id:
            menu = Menu.objects.get(
                meal_id=meal.id,
                food_id=meal.soup.id,
            )
            menu.food_id = soup_id
            menu.save()

        meal.update_side_dish_id_set(new_side_dish_id_set)

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

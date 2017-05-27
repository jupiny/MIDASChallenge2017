from django.views.generic.base import View
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.db import transaction

from date.models import Date
from food.models import Food
from menu.models import Menu
from meal.models import Meal


BREAKFAST = 1
LUNCH = 2
DINNER = 3

RICE = 1
SOUP = 2
SIDE_DISH = 3
DESSERT = 4


class MealCreateView(View):
    meal_type = None
    template_name = None

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date = get_object_or_404(Date, date=date)
        return render(
            request,
            self.template_name,
            context={
                'rice_set': Food.objects.filter(food_type=RICE),
                'soup_set': Food.objects.filter(food_type=SOUP), 'side_dish_set': Food.objects.filter(food_type=SIDE_DISH),
                'year': year,
                'month': month,
                'day': day,
             }
        )

    def post(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date = get_object_or_404(Date, date=date)

        rice_id = request.POST.get('rice')
        soup_id = request.POST.get('soup')
        side_dish_id_set = request.POST.getlist('side_dish')

        with transaction.atomic():
            meal = Meal.objects.create(
                date=date,
                meal_type=self.meal_type,
            )
            Menu.objects.create(
                meal=meal,
                food=Food.objects.get(pk=rice_id),
            )
            Menu.objects.create(
                meal=meal,
                food=Food.objects.get(pk=soup_id),
            )
            Menu.objects.bulk_create([
                Menu(meal_id=meal.id, food_id=side_dish_id)
                for side_dish_id in side_dish_id_set 
            ])
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


class BreakfastCreateView(MealCreateView):
    meal_type = BREAKFAST
    template_name = 'meal/new_breakfast.html'


class LunchCreateView(MealCreateView):
    meal_type = LUNCH
    template_name = 'meal/new_lunch.html'


class DinnerCreateView(MealCreateView):
    meal_type = DINNER
    template_name = 'meal/new_dinner.html'

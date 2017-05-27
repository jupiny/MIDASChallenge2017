from django.db import models

from menu.models import Menu
from food.constants import RICE, SOUP, SIDE_DISH, DESSERT
from meal.constants import BREAKFAST, LUNCH, DINNER


MEAL_TYPE_CHOICES = (
    (BREAKFAST, '아침'),
    (LUNCH, '점심'),
    (DINNER, '저녁'),
)


class Meal(models.Model):
    date = models.ForeignKey('date.Date')
    meal_type = models.IntegerField(choices=MEAL_TYPE_CHOICES)

    def __str__(self):
        return '{date} {meal_type}'.format(
            date=self.date.date_to_str,
            meal_type=self.get_meal_type_display(),
        )

    @property
    def rice(self):
        return self.food_set.filter(food_type=RICE).last()

    @property
    def soup(self):
        return self.food_set.filter(food_type=SOUP).last()

    @property
    def side_dish_set(self):
        return self.food_set.filter(food_type=SIDE_DISH)

    @property
    def dessert_set(self):
        return self.food_set.filter(food_type=DESSERT)

    @property
    def all_calories(self):
        all_calories = 0
        for food in self.food_set.all():
            all_calories += food.calorie
        return all_calories


    def update_side_dish_id_set(self, new_side_dish_id_set):
        cur_side_dish_id_set = self.side_dish_set.values_list('id', flat=True)

        insert_side_dish_id_set = list(set(new_side_dish_id_set)-set(cur_side_dish_id_set))
        delete_side_dish_id_set = list(set(cur_side_dish_id_set)-set(new_side_dish_id_set))

        if insert_side_dish_id_set:
            Menu.objects.bulk_create([
                Menu(food_id=side_dish_id, meal_id=self.id)
                for side_dish_id in insert_side_dish_id_set
            ])
        if delete_side_dish_id_set:
            self.menu_set.filter(food_id__in=delete_side_dish_id_set).delete()

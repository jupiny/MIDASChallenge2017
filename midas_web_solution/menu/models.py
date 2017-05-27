from django.db import models


class Menu(models.Model):
    meal = models.ForeignKey('meal.Meal')
    food = models.ForeignKey('food.Food')

    def __str__(self):
        return '{meal} - {food}'.format(
            meal=str(self.meal),
            food=str(self.food),
        )

from django.db import models
from django.contrib.auth.models import User


class Eating(models.Model):
    user = models.ForeignKey(User)
    meal = models.ForeignKey('meal.Meal')

    def __str__(self):
        return '{user} - {meal}'.format(
            user=self.user.username,
            meal=str(self.meal),
        )

from django.db import models


BREAKFAST = 1
LUNCH = 2
DINNER = 3


class Date(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date_to_str

    @property
    def date_to_str(self):
        return self.date.strftime('%Y-%m-%d')

    @property
    def breakfast_meal(self):
        return self.meal_set.filter(meal_type=BREAKFAST).last()

    @property
    def lunch_meal(self):
        return self.meal_set.filter(meal_type=LUNCH).last()

    @property
    def dinner_meal(self):
        return self.meal_set.filter(meal_type=DINNER).last()

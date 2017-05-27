from django.db import models


BREAKFAST = 1
LUNCH = 2
DINNER = 3

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

from django.db import models


RICE = 1
SOUP = 2
SIDE_DISH = 3
DESSERT = 4

FOOD_TYPE_CHOICES = (
    (RICE, '밥'),
    (SOUP, '국'),
    (SIDE_DISH, '반찬'),
    (DESSERT, '디저트'),
)


class Food(models.Model):
    meal_set = models.ManyToManyField(
        'meal.Meal',
        related_name='food_set',
        through='menu.Menu',
    )
    name = models.CharField(max_length=100)
    food_type = models.IntegerField(choices=FOOD_TYPE_CHOICES)
    calorie = models.IntegerField()
    origin = models.CharField(max_length=100)
    image = models.ImageField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return 'http://placehold.it/350x150'



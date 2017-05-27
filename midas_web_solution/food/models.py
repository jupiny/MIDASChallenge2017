from django.db import models


class Food(models.Model):
    meal_set = models.ManyToManyField(
        'meal.Meal',
        related_name='food_set',
        related_query_name='food',
    )
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()
    origin = models.CharField(max_length=100)
    image = models.ImageField(
        blank=True,
        null=True,
    )

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return 'http://placehold.it/350x150'

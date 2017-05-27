from django.db import models


class Date(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date_to_str

    @property
    def date_to_str(self):
        return self.date.strftime('%Y-%m-%d')

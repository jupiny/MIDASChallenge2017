from django.db import models


class Date(models.Model):
    date = models.DateField(unique=True)

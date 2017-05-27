from django.contrib import admin

from .models import Eating


class EatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Eating, EatingAdmin)

from django.contrib import admin

from .models import Date


class DateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Date, DateAdmin)

from django.views.generic.base import View
from django.shortcuts import render

from date.models import Date


class DateListView(View):

    def get(self, request, *args, **kwargs):
        date_set = Date.objects.all()
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            date_set = date_set.filter(date__range=[start_date, end_date])
        return render(
            request,
            'date/list.html',
            context={
                'date_set': date_set.order_by('date'), 
                'start_date': start_date, 
                'end_date': end_date, 
            }
        )

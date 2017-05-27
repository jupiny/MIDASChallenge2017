from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from date.models import Date


class DateAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date, created = Date.objects.get_or_create(date=date)
        content = {
                'breakfast_meal_eating_count': date.breakfast_meal.eating_set.count(),
                'lunch_meal_eating_count': date.lunch_meal.eating_set.count(),
                'dinner_eating_count': date.dinner_meal.eating_set.count(),
        }
        return Response(
            content,
            status.HTTP_200_OK,
        )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from date.models import Date


class UserDateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date, created = Date.objects.get_or_create(date=date)
        breakfast_meal_eating_count = 0
        lunch_meal_eating_count = 0
        dinner_meal_eating_count = 0
        if date.breakfast_meal:
            breakfast_meal_eating_count = date.breakfast_meal.eating_set.filter(user_id=request.user.id).count()
        if date.lunch_meal:
            lunch_meal_eating_count = date.lunch_meal.eating_set.filter(user_id=request.user.id).count()
        if date.dinner_meal:
            dinner_meal_eating_count = date.dinner_meal.eating_set.filter(user_id=request.user.id).count()

        content = {
                'breakfast_meal_eating_count': breakfast_meal_eating_count, 
                'lunch_meal_eating_count': lunch_meal_eating_count, 
                'dinner_eating_count': dinner_meal_eating_count, 
        }
        return Response(
            content,
            status.HTTP_200_OK,
        )


class AdminDateAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')
        date = year+"-"+month+"-"+day
        date, created = Date.objects.get_or_create(date=date)

        breakfast_meal_eating_count = 0
        lunch_meal_eating_count = 0
        dinner_meal_eating_count = 0
        if date.breakfast_meal:
            breakfast_meal_eating_count = date.breakfast_meal.eating_set.count()
        if date.lunch_meal:
            lunch_meal_eating_count = date.lunch_meal.eating_set.count()
        if date.dinner_meal:
            dinner_meal_eating_count = date.dinner_meal.eating_set.count()

        content = {
                'breakfast_meal_eating_count': breakfast_meal_eating_count, 
                'lunch_meal_eating_count': lunch_meal_eating_count, 
                'dinner_eating_count': dinner_meal_eating_count, 
        }
        return Response(
            content,
            status.HTTP_200_OK,
        )

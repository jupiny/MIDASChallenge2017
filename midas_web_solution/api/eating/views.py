from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from eating.models import Eating


class EatingAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        meal_id = request.POST.get('meal_id')
        Eating.objects.create(
            user_id=request.user.id,
            meal_id=meal_id,
        )
        return Response(status.HTTP_201_CREATED)

    def delete(self, request, format=None):
        meal_id = request.POST.get('meal_id')
        eating = Eating.objects.get(
            user_id=request.user.id,
            meal_id=meal_id,
        )
        eating.delete()
        return Response(status.HTTP_204_NO_CONTENT)

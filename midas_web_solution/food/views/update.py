from django.views.generic.base import View 
from django.shortcuts import redirect

from food.models import Food
from users.mixins import AdminRequiredMixin


class FoodUpdateView(AdminRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        calorie = request.POST.get('calorie')
        origin = request.POST.get('origin')
        food_type = request.POST.get('food_type')
        image = request.FILES.get('image')

        food = Food.objects.get(pk=kwargs.get('pk'))
        food.name = name
        food.calorie = calorie
        food.origin = origin 
        food.food_type=food_type
        if image:
            food.image = image
        food.save()
        return redirect('food:list')


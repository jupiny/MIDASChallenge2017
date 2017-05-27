from django.views.generic.base import View 
from django.shortcuts import redirect

from food.models import Food
from users.mixins import AdminRequiredMixin


class FoodCreateView(AdminRequiredMixin, View):
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        calorie = request.POST.get('calorie')
        origin = request.POST.get('origin')
        food_type = request.POST.get('food_type')
        image = request.FILES.get('image')
        food = Food.objects.create(
            name=name,
            calorie=calorie,
            origin=origin,
            food_type=food_type,
            image=image,
        )
        return redirect('food:list')

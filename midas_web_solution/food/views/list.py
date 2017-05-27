from django.views.generic.list import ListView

from food.models import Food


class FoodListView(ListView):
    model = Food
    template_name = 'food/list.html'
    context_object_name = 'foods'

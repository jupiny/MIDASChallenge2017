from django.views.generic.detail import DetailView 

from food.models import Food


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food/detail.html'
    context_object_name = 'food'

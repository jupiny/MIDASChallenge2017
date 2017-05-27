from django.views.generic.detail import DetailView 

from food.models import Food


class FoodEditView(DetailView):
    model = Food
    template_name = 'food/edit.html'
    context_object_name = 'food'

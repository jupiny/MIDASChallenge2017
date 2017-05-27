from django.views.generic.detail import DetailView 

from food.models import Food
from users.mixins import AdminRequiredMixin


class FoodEditView(AdminRequiredMixin, DetailView):
    model = Food
    template_name = 'food/edit.html'
    context_object_name = 'food'

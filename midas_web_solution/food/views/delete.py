from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from food.models import Food


class FoodDeleteView(DeleteView):
    model = Food
    success_url = reverse_lazy('food:list')
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

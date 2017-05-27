from django.views.generic.base import TemplateView 


class FoodNewView(TemplateView):
    template_name = 'food/new.html'

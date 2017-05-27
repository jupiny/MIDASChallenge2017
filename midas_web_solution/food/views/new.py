from django.views.generic.base import TemplateView 

from users.mixins import AdminRequiredMixin


class FoodNewView(AdminRequiredMixin, TemplateView):
    template_name = 'food/new.html'

from django import template

from eating.models import Eating


register = template.Library()


@register.simple_tag
def is_eating(user_id, meal_id):
    try:
       eating = Eating.objects.get(user_id=user_id, meal_id=meal_id)
    except Eating.DoesNotExist:
       eating  = None
    return eating

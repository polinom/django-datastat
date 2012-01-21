from django import template
from django.core.cache import cache
from django.core import urlresolvers
from django.db.models import get_model

register = template.Library()
from pprint import pprint

@register.simple_tag
def statmodel(modelget_model(app_label, model_name)):
    model = get_model(*tuple(model['admin_url'].split('/')[:2]))
    return model


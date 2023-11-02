from django import template
from customadmin.models import CustomUser, Item


register = template.Library()


@register.inclusion_tag("customadmin/row.html")
def render_row(obj, fields):
    data = {}
    for field in fields:
        try:
            data[field] = obj.__dict__[field]
        except KeyError:
            data[field] = obj.__dict__[field + "_id"]

    return {
        "data": data,
        "object": obj,
    }

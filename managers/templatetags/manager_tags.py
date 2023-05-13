from django import template

register = template.Library()


@register.simple_tag
def add_attr(field, key, value):
    attrs = {}
    attrs[key] = value
    return field.as_widget(attrs=attrs)
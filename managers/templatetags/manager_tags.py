from django import template
from warmuppers.models import EmailAddressAssignment

register = template.Library()


@register.simple_tag
def add_attr(field, key, value):
    attrs = {}
    attrs[key] = value
    return field.as_widget(attrs=attrs)

@register.filter
def checkassignment(emailid, warmupperid):
    return EmailAddressAssignment.objects.filter(email=emailid, warmupper=warmupperid).exists()
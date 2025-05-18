from django import template

register = template.Library()

@register.filter(name="bleach")
def bleach(value): # Only one argument.
    """Converts # into ' '"""
    return value.replace('#', ' ')


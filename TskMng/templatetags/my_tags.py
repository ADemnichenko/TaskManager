from django import template

register = template.Library()

@register.filter(name="split")
def split(str,splitter):
    return str.split(splitter)[-1]
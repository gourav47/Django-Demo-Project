from django import template
import datetime
register=template.Library()

@register.simple_tag(name="get_date")
def get_date():
    now = datetime.datetime.now()
    return now

@register.filter(name="quotes")
def quotes(value):
    s='"'+value+'"'
    return s

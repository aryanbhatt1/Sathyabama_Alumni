from django import template
import calendar

from django.urls import reverse

register = template.Library()


@register.filter
def month_filter(month):
    month_number = int(month)
    return calendar.month_name[month_number]

@register.simple_tag
def is_active(request, url):
    # Main idea is to check if the url and the current path is a match
    if request.path in reverse(url):
        return "active"
    return ""
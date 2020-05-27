from django import template

import string # python package

register = template.Library()

@register.filter
def format_poll(sentence):
    return "~" + string.capwords(sentence) + "~"
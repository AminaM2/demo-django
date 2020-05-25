from django import template

import string # python package

register = template.Library()

@register.filter
def formattitle(sentence):
    return "-" + string.capwords(sentence) + "-"
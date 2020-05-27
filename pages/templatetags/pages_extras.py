from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

#create a file in following path = <appname>\templatetags\<appname>_extras.py

#how to use in templates: 
#                   {% load <filter_name> %}   
#                   {{param1|<filter_name>:param2}}
#                   app that contains the custom tags must be in INSTALLED_APPS in order for the {% load %} tag to work
#                   create an __init__.py file in the templatetags folder to ensure the directory is treated as a Python package

# additonnal doc: https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/
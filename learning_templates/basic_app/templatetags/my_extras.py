#EXAMPLE OF CREATING YOUR OWN TEMPLATE FILTERS

from django import template

register = template.Library()

@register.filter(name = 'cut') #passing as parameter the name of filter function you created.
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

#register.filter('cut', cut)

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name_or_path, startswith=False):
    """
    Usage:
    {% active 'core:home' %}                 -> exact match by reverse()
    {% active '/properties/' True %}         -> match by path startswith
    {% active 'core:properties' True %}      -> reverse then startswith
    """
    request = context.get('request')
    if not request:
        return ''

    try:
        # Try treating first arg as a url name and reverse it
        target = reverse(url_name_or_path)
    except NoReverseMatch:
        # Fallback: treat it as a literal path
        target = url_name_or_path

    if startswith:
        return 'active' if request.path.startswith(target) else ''
    return 'active' if request.path == target else ''
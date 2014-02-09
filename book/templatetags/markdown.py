from markdown2 import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.text import force_unicode

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def markdown2(value):
    return markdown(force_unicode(value),
                     extras=['wiki-tables',
                             'pyshell',
                             'fenced-code-blocks'])

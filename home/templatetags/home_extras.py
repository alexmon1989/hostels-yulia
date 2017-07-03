from django import template
from home.models import Footer
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def footer_text():
    footer = Footer.objects.get()
    return mark_safe(footer.short_text)


@register.simple_tag
def footer_telephones():
    footer = Footer.objects.get()
    return mark_safe(footer.telephones)

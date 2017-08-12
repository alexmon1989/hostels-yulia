from django import template
from home.models import Footer, GoogleAnalyticsCode
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def google_analytics_html():
    google_analytics, created = GoogleAnalyticsCode.objects.get_or_create()
    return mark_safe(google_analytics.code)


@register.simple_tag
def footer_text():
    footer = Footer.objects.get()
    return mark_safe(footer.short_text)


@register.simple_tag
def footer_telephones():
    footer = Footer.objects.get()
    return mark_safe(footer.telephones)

from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from djangoseo.admin import register_seo_admin, auto_register_inlines
from hostels_site.seo import MyMetadata

from home.models import Service, AboutUs, Footer, GoogleAnalyticsCode


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')

admin.site.register(Service, ServicesAdmin)
admin.site.register(AboutUs, SingleModelAdmin)
admin.site.register(Footer, SingleModelAdmin)
admin.site.register(GoogleAnalyticsCode, SingleModelAdmin)
register_seo_admin(admin.site, MyMetadata)
auto_register_inlines(admin.site, MyMetadata)

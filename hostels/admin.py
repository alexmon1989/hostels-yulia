from django.contrib import admin
from hostels.models import Hostel, Service, Price, Photo


class PriceInline(admin.TabularInline):
    model = Price


class PhotosInline(admin.TabularInline):
    model = Photo


class HostelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')
    inlines = [PhotosInline, PriceInline]


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Hostel, HostelsAdmin)
admin.site.register(Service, ServicesAdmin)

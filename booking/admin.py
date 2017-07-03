from django.contrib import admin
from booking.models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'email', 'is_processed', 'created_at', 'updated_at')
    list_editable = ('is_processed', )

    def has_add_permission(self, request):
        return False

admin.site.register(Booking, BookingAdmin)

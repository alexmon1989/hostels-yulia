from django.contrib import admin

from feedbacks.models import Feedback


class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'position', 'is_moderated', 'is_published', 'is_on_main_page', 'created_at', 'updated_at')

admin.site.register(Feedback, FeedbacksAdmin)

from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at')

admin.site.register(News, NewsAdmin)

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from news.models import News
from hostels.models import Hostel


class StaticSitemap(Sitemap):
    def items(self):
        return [
            'home',
            'contacts:contacts_index',
            'feedbacks:feedback_index',
            'prices:prices_index',
        ]

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    def items(self):
        return News.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class HostelsSitemap(Sitemap):
    def items(self):
        return Hostel.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

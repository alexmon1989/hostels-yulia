"""hostels_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import index
from django.conf import settings
from django.conf.urls.static import static
from hostels_site.sitemap import StaticSitemap, NewsSitemap, HostelsSitemap
from django.contrib.sitemaps.views import sitemap

handler404 = 'home.views.error_404'


sitemaps = {
    'static': StaticSitemap,
    'news': NewsSitemap,
    'hostels': HostelsSitemap,
}

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^hostels/', include('hostels.urls')),
    url(r'^prices/', include('prices.urls')),
    url(r'^feedback/', include('feedbacks.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^booking/', include('booking.urls')),
    url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps}),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

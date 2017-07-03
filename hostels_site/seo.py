from djangoseo import seo


class MyMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()
    heading = seo.Tag(name="h1")

    class Meta:
        seo_models = ('news.News', 'hostels.Hostel')
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
        backends = ('path', 'modelinstance')

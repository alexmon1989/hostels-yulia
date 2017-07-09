from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Service(models.Model):
    title = models.CharField('Название', max_length=255)
    icon = models.CharField('Иконка', max_length=255)
    description = models.CharField('Описание', max_length=255)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Список сервисов'


class Hostel(models.Model):
    """Модель хостела."""
    slug = models.CharField('Slug', max_length=255)
    title = models.CharField('Название', max_length=255)
    short_description = RichTextUploadingField('Короткое описание')
    full_description = RichTextUploadingField('Полное описание')
    image = models.ImageField(
        'Изображение',
        upload_to='hostels/',
        null=True,
        blank=True,
        help_text='Оптимальный размер для изображения - 339px * 216px'
    )
    code_google_maps = models.TextField('HTML-код карты Google', null=True, blank=True)
    address = RichTextUploadingField('Адрес, телефоны', max_length=255)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hostels:hostel_details', args=[str(self.slug)])

    class Meta:
        ordering = ['id']
        verbose_name = 'Хостел'
        verbose_name_plural = 'Список хостелов'


class Price(models.Model):
    title = models.CharField('Название', max_length=255)
    value = models.IntegerField('Значение, грн')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Photo(models.Model):
    title = models.CharField('Название', max_length=255, default='Фото')
    image = models.ImageField(
        'Фото',
        upload_to='hostels/'
    )
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

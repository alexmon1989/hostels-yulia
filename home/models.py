from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    """Модель услуг (преимуществ)."""
    title = models.CharField('Название', max_length=255)
    icon = models.CharField('Иконка', max_length=255)
    description = models.CharField('Описание', max_length=255)
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class AboutUs(models.Model):
    title = models.CharField('Название', max_length=255)
    image = models.ImageField(
        'Изображение',
        upload_to='about/',
        null=True,
        blank=True
    )
    head_text = models.CharField('Заглавный текст', max_length=255)
    text = RichTextUploadingField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Footer(models.Model):
    short_text = RichTextUploadingField('Короткое описание')
    telephones = RichTextUploadingField('Телефоны')

    def __str__(self):
        return 'Подвал (footer)'

    class Meta:
        verbose_name = 'Подвал (footer)'
        verbose_name_plural = 'Подвал (footer)'


class GoogleAnalyticsCode(models.Model):
    code = models.TextField('Код HTML')

    def __str__(self):
        return 'Код HTML Google Analytics'

    class Meta:
        verbose_name = 'Google Analytics (HTML код)'
        verbose_name_plural = 'Google Analytics (HTML код)'

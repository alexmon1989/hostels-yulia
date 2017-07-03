from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class News(models.Model):
    """Модель новостей."""
    title = models.CharField('Заголовок', max_length=255)
    short_text = RichTextUploadingField('Короткий текст')
    full_text = RichTextUploadingField('Полный текст')
    image = models.ImageField(
        'Изображение',
        upload_to='news/',
        null=True,
        blank=True,
        help_text='Оптимальный размер для изображения - 973px * 615px'
    )
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Список новостей'
        ordering = ['-created_at']

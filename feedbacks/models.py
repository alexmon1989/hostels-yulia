from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Feedback(models.Model):
    """Модель хостела."""
    client_name = models.CharField('Имя клиента', max_length=255)
    position = models.CharField('Должность', max_length=255, null=True, blank=True)
    text = models.TextField('Текст отзыва')
    image = models.ImageField(
        'Фото клиента',
        upload_to='feedbacks/',
        null=True,
        blank=True
    )
    is_published = models.BooleanField('Опубликовано', default=False)
    is_on_main_page = models.BooleanField('Опубликовано на главной странице', default=False)
    is_moderated = models.BooleanField('Промодерировано', default=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.client_name, self.position)

    def save(self, *args, **kwargs):
        if self.image:
            # Opening the uploaded image
            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            im.thumbnail((100, 100), Image.ANTIALIAS)

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                            sys.getsizeof(output), None)

        super(Feedback, self).save()

    @staticmethod
    def get_new_count():
        return Feedback.objects.filter(is_moderated=False).count()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Список отзывов'

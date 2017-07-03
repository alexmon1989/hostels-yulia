from django.db import models


class Booking(models.Model):
    name = models.CharField('Имя', max_length=255)
    telephone = models.CharField('Телефон', max_length=255)
    email = models.CharField('E-Mail', max_length=255, null=True, blank=True)
    message = models.TextField('Сообщение', null=True, blank=True)
    is_processed = models.BooleanField('Обработано', default=False)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_new_count():
        return Booking.objects.filter(is_processed=False).count()

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

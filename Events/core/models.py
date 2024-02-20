from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events')

    event_date = models.DateTimeField()

    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return f'Событие {self.title} {self.pk}'

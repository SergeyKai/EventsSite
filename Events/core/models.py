from django.db import models


class Speaker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    image = models.ImageField(upload_to='speaker')

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'

    def __str__(self):
        return f'Спикер {self.first_name} {self.last_name} <{self.pk}>'


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events')

    event_date = models.DateTimeField()

    create_date = models.DateTimeField(auto_now=True)

    speakers = models.ManyToManyField(Speaker, related_name='events')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['event_date', 'title']

    def __str__(self):
        return f'Событие {self.title} <{self.pk}>'
